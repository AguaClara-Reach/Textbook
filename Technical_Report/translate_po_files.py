from googletrans import Translator
import polib
import re
import os
import glob
import time
import spacy

nlp = spacy.load("en_core_web_sm")

EXCLUDED_NAMES = {"AguaClara Reach", "AguaClara", "San Juan Planes", "Agua Para el Pueblo", "Church of Jesus Christ of Latter-day Saints"}

MANUAL_TRANSLATIONS = {
    "clarifier": "clarificador",
    "Clarifier": "Clarificador",
    "Diffusers" : "Difusores",
    "Authors" : "Autores",
    # Add more custom translations as needed
}

# def extract_rst_elements(text):
#     rst_elements = []

#     # Catch all inline reST roles like :sub:`...`, :math:`...`, etc.
#     role_re = re.compile(r':[a-zA-Z0-9_]+:`[^`]*`')
#     # Catch inline links and references
#     link_re = re.compile(r'`[^`]+? <[^>]+>`_')
#     ref_re = re.compile(r':ref:`[^`]+`')

#     def _mask(m):
#         rst_elements.append(m.group(0))
#         return f"__rst{len(rst_elements)}__"

#     text = role_re.sub(_mask, text)
#     text = link_re.sub(_mask, text)
#     text = ref_re.sub(_mask, text)

#     return text, rst_elements

def extract_rst_elements(text):
    rst_elements = []

    # Combined pattern:
    # 1. reST roles: :role:`content`
    # 2. reST hyperlinks: `text <url>`_
    # 3. plain URLs
    pattern = r"""
        (                           # Group 1: Any one of the following...
            :\w+:`[^`]+?`           # reST role like :ref:`label`, :sub:`text`, etc.
            |`[^`]+? <[^>]+?>`_     # reST hyperlink like `text <url>`_
            |https?://[^\s<>()]+    # plain URL (avoid trailing punctuation)
        )
    """

    def replacer(match):
        rst_elements.append(match.group(0))
        return f"__rst{len(rst_elements)}__"

    protected_text = re.sub(pattern, replacer, text, flags=re.VERBOSE)
    return protected_text, rst_elements

def restore_rst_elements(text, rst_elements):
    for i, val in enumerate(rst_elements):
        pattern = re.compile(re.escape(f"__rst{i+1}__"), re.IGNORECASE)
        text = pattern.sub(val, text)
    return text


def apply_manual_substitutions(text):
    """
    Applies manual translations for specific words.
    """
    # print(f"Original text before manual substitution: '{text}'")
    
    manually_translated_part = text  # Start with the full text to modify

    for original, translated in MANUAL_TRANSLATIONS.items():
        # Replace only whole words using word boundaries if needed
        pattern = rf"\b{re.escape(original)}\b"
        manually_translated_part = re.sub(pattern, translated, manually_translated_part)
        # print(f"After replacing '{original}' with '{translated}': '{manually_translated_part}'")
    
    return manually_translated_part


def contains_excluded_content(text):
    """
    Checks if text contains:
    - :numref: references
    - |substitutions|
    - :sub: references
    - URLs (http, https)
    - reStructuredText references (:ref:, .. _link:)
    - Manually defined excluded names
    """
    patterns = [
        r":numref:`[^`]+`",  # :numref:
        r"\|[^|]+\|",        # |substitutions|
        r":sub:`[^`]+`",     # :sub:
        r"https?://\S+",     # URLs
        r":ref:`[^`]+`",     # reST :ref:
        r"\.\. _[^:]+:",     # reST ".. _link:"
    ]

        # Debugging output to check what text is being passed
    # print(f"Checking text: '{text}'")
    
    for pattern in patterns:
        if re.search(pattern, text):
            return True
    
    for name in EXCLUDED_NAMES:
        if name in text:
            # If the exact word exists in the text, mark it as excluded
            if re.search(rf"\b{name}\b", text):  # Use word boundaries (\b)    
                # print(f"Excluded name found: {name} in '{text}'")  # Debugging output
                return True
    
    return False

# Base pattern to exclude special reST content
base_pattern = (
    r"(:numref:`[^`]+`|"         # numref directive
    r"\|[^|]+\||"                # substitution reference
    r":sub:`[^`]+`|"             # sub directive
    r"https?://\S+|"             # URLs
    r":ref:`[^`]+`|"             # ref directive
    r"\.\. _[^:]+:|"             # hyperlink targets
    r"`[^<]+<[^>]+>`_)"          # reST hyperlinks
)

# Add excluded names as literal alternatives
escaped_names = [re.escape(name) for name in sorted(EXCLUDED_NAMES, key=len, reverse=True)]
name_pattern = "|".join(escaped_names)

# Full combined pattern
full_pattern = f"({base_pattern}|{name_pattern})"

# Compile the regex
combined_regex = re.compile(full_pattern)

def split_preserving_excluded(text):
    """
    Splits the input text into a list where each part is either:
    - an excluded element (link, inline directive, name), or
    - plain translatable text.
    """
    
    parts = []
    last_idx = 0

    for match in combined_regex.finditer(text):
        start, end = match.span()

        # Add translatable text before match
        if last_idx < start:
            parts.append(text[last_idx:start])

        # Add the excluded match itself
        parts.append(text[start:end])
        last_idx = end

    # Add any remaining translatable text
    if last_idx < len(text):
        parts.append(text[last_idx:])

    return [part for part in parts if part]  # Remove empty strings


def preserve_formatting(original, translated):
    bold_pattern = re.compile(r"\*{2}(.+?)\*{2}")
    def fix_bold(match):
        inner = match.group(1).strip()
        return f"**{inner}**"
    translated = re.sub(r"\*{2}\s*(.+?)\s*\*{2}", fix_bold, translated)
    return translated


def reposition_excluded_names(text):
    excluded_names = sorted(EXCLUDED_NAMES, key=lambda x: -len(x))  # prioritize longest names first
    for name in excluded_names:
        name_escaped = re.escape(name)

        # Match (optional article) + excluded name + following words — include leading space
        pattern = rf'(\b(?:a|an)\s+)?({name_escaped})\s+((?:[^\.\,\n;:]+))'

        def replacer(match):
            article = match.group(1)
            excluded = match.group(2)
            following = match.group(3)

            full_match_span = match.span()
            char_before_match = text[full_match_span[0] - 1] if full_match_span[0] > 0 else '∅'
            # print(f"\nFULL MATCH: '{match.group(0)}' (span {full_match_span[0]}-{full_match_span[1]})")
            # print(f"Matched: article='{article}', excluded='{excluded}', following='{following}'")
            # print(f"Character before match: '{char_before_match}'")

            doc = nlp(following)
            noun_chunks = list(doc.noun_chunks)

            if noun_chunks and noun_chunks[0].start == 0:
                # Use noun chunk normally
                first_chunk = noun_chunks[0]
                first_chunk_text = doc[first_chunk.start:first_chunk.end].text
                remaining_text = doc[first_chunk.end:].text.strip()
                # print(f"Using spaCy noun chunk: '{first_chunk_text}' + '{excluded}' + '{remaining_text}'")

                result = f"{article or ''}{first_chunk_text} {excluded} {remaining_text}".strip()
                # print(f"Result after substitution: '{result}'")
                return result

            # Fallback: try manually identifying a noun phrase from token 0
            collected = []
            for token in doc:
                # print(f"Token: '{token.text}', POS: {token.pos_}, Tag: {token.tag_}")
                if token.pos_ in {"ADJ", "NOUN", "PROPN", "DET"} or token.tag_ == "VBG":
                    collected.append(token)
                else:
                    break  # stop at first unrelated POS

            if collected:
                first_chunk_text = " ".join([t.text for t in collected])
                remaining_text = doc[len(collected):].text.strip()
                # print(f"Collected tokens: {[t.text for t in collected]}")
                # print(f"Using manual chunk: '{first_chunk_text}' + '{excluded}' + '{remaining_text}'")
                # print(f"Before returning: First chunk text = '{first_chunk_text}', Excluded = '{excluded}', Remaining text = '{remaining_text}'")

                result = f"{article or ' '}{first_chunk_text} {excluded} {remaining_text}".strip()
                # print(f"Result after substitution: '{result}'")
                return result

            # print("No noun chunk or valid manual chunk — keeping original.")
            return match.group(0)

        # Apply the substitution
        text = re.sub(pattern, replacer, text)

        # print(f"\nText after processing '{name}':\n{text}\n")

    return text





def fix_rst_roles(text):
    # Fix spaces inside and after reST roles like ": numref : `label`"
    # 1. Remove space after the first colon
    text = re.sub(r':\s+(\w+):', r':\1:', text)
    # 2. Remove space between role and backtick
    text = re.sub(r':(\w+):\s+`', r':\1:`', text)
    return text

def preserve_spaces(text):
    """
    Ensures spaces are properly preserved where needed, especially between sentences and after punctuation.
    """
    # Add a space after punctuation marks where needed (e.g., after periods and commas)
    text = re.sub(r"([.,;!?:])(\S)", r"\1 \2", text)  # Ensure space after punctuation if no space

    # Ensure there's space after excluded names when moved to the end of a noun phrase
    for name in EXCLUDED_NAMES:
        # Ensure there’s a space after the name if it’s followed directly by another word
        text = re.sub(rf"(\b{re.escape(name)})\s*(\w)", r"\1 \2", text)
    
    return text


def translate_text(text, target_lang='es'):
    """
    Translates text while skipping specific elements like manually translated words or reST hyperlinks.
    """
    print(f"Original text: '{text}'")  # Debugging step

    protected_text, rst_elements = extract_rst_elements(text)


    translator = Translator()
    retries = 3  # number of retries
    delay = 2    # delay between retries in seconds

    # Adjust articles *before* splitting and translation
    # print(f"Original text before adjusting articles: '{text}'")  # Debugging step
    protected_text = reposition_excluded_names(protected_text)
    # print(f"Adjusted text after repositioning excluded names: '{text}'")  # Debugging step
    parts = split_preserving_excluded(protected_text)
    # print(f"Original text split into parts: {parts}")  # Debugging step

    translated_parts = []

    for part in parts:
        print(f"Checking part: '{part}'")  # Debugging step

# Skip translating if part contains excluded content or an excluded name
        if contains_excluded_content(part) or any(name in part for name in EXCLUDED_NAMES):
            print(f"Skipping part (excluded content): {part}")
            translated_parts.append(part)
        else:
            success = False
            for attempt in range(retries):
                try:
                    print(f"Before manual substitution: '{part}'")
                    part_to_translate = apply_manual_substitutions(part)
                    print(f"After manual substitution: '{part_to_translate}'")

                    # Separate the part into manual and translatable portions
                    manually_translated = part_to_translate
                    remaining_text = ""

                    # If any manual translations exist, replace them
                    for original, translated in MANUAL_TRANSLATIONS.items():
                        if original in manually_translated:
                            # Replace manually translated part
                            manually_translated = manually_translated.replace(original, translated)

                            # If the original part was found, set remaining_text to the original part
                    # Now, the remaining part to translate is just what wasn't manually translated
                    remaining_text = manually_translated

                    if '**' in part:
                        bold_matches = re.findall(r'\*\*(.*?)\*\*', part)
                        print(f"Found bold content: {bold_matches}")

                    # If this is a reST hyperlink, handle it separately
                    if '`' in part and '<' in part:
                        # Handle reST hyperlink: `visible text <URL>`
                        visible_text = part.split('<')[0][1:].strip()
                        translated_visible = translator.translate(visible_text, dest=target_lang).text
                        translated_part = f"`{translated_visible} <{part.split('<', 1)[1]}"
                        translated_parts.append(translated_part)
                    else:
                        # Translate the remaining text (non-manual and non-reST parts)
                        if remaining_text:  # Ensure there's text left to translate
                            result = translator.translate(remaining_text, dest=target_lang)
                            if result and hasattr(result, "text"):
                                translated = result.text

                                 # ✅ Show result of translation
                                print(f"Translated: '{remaining_text}' → '{translated}'")

                                 # ✅ Check bold in translated result
                                if '**' in translated:
                                    bold_in_translated = re.findall(r'\*\*(.*?)\*\*', translated)
                                    print(f"Bold segments in translation: {bold_in_translated}")

                                if part.startswith(" "):
                                    translated = " " + translated
                                if part.endswith(" "):
                                    translated = translated + " "

                                print(f"Translating: '{remaining_text}' -> '{translated}'")  # Debugging step
                                # Append only the translated text (not the manually translated part)
                                translated_parts.append(translated)
                            else:
                                translated_parts.append(remaining_text)  # If no translation, just append remaining part
                        else:
                            translated_parts.append(remaining_text)  # If nothing to translate, keep the remaining part

                    success = True
                    break  # Break out of retry loop on success
                except Exception as e:
                    print(f"[Attempt {attempt + 1}] Error translating '{part}': {e}")
                    time.sleep(delay)

            if not success:
                print(f"Failed to translate after {retries} retries. Keeping original: '{part}'")
                translated_parts.append(part)

    print(f"Translated parts: {translated_parts}")  # Debugging step
    translated_text = "".join(translated_parts)
    translated_text = preserve_spaces(translated_text)
    translated_text = preserve_formatting(protected_text, translated_text)
    translated_text = fix_rst_roles(translated_text)
    translated_text = restore_rst_elements(translated_text, rst_elements)


    print(f"Final translated text: {translated_text}")  # Debugging step
    return translated_text


def translate_po_file(input_po_file, target_lang='es'):
    po = polib.pofile(input_po_file)
    
    for entry in po:
        if entry.msgstr == "" or entry.msgstr == entry.msgid:
            translated = translate_text(entry.msgid, target_lang)
            entry.msgstr = translated
            print(f"Translated: '{entry.msgid}' -> '{entry.msgstr}'")
    
    po.save(input_po_file)
    print(f"Translated file saved as: {input_po_file}")

def translate_po_files_in_directory(directory_path, target_lang='es'):
    po_files = glob.glob(os.path.join(directory_path, '*.po'))
    
    if not po_files:
        print("No .po files found in the directory.")
        return

    for input_po_file in po_files:
        print(f"Processing file: {input_po_file}")
        translate_po_file(input_po_file, target_lang)

# po_directory = 'po_files/es/LC_MESSAGES'
# translate_po_files_in_directory(po_directory, target_lang='es')

# po_file_path = 'po_files/es/LC_MESSAGES/Chemical_Dosing.po' #for quick check
# translate_po_file(po_file_path, target_lang='es') #for quick check

test_text_01 = "Design information for the AguaClara clarifier is available in `the Clarifier Design chapter of The Physics of Water Treatment Design <https://aguaclara.github.io/Textbook/Clarification/Clarifier_Design.html>`_."
test_text_02 = "**This is the scientific method** yes"
test_text_03 = ":sub:`($..et.lfom.Qm_max) no-sub`"
test_text_04 = "This is a test with a URL: https://example.com and a reference: :ref:`example`."
test_text_05 = "This system has the characteristic of maintaining a constant chemical **dosage** even as the flow rate through the plant varies."
test_text_06 = "Copyright 2025 AguaClara Reach"
test_text_07 = "The tables below summarize the raw water quality parameters for which AguaClara drinking water treatment technologies are appropriate."
test_text_08 = "AguaClara treatment technologies include trash and grit removal, flow measurement, chemical dosing, rapid mix, flocculation, floc filter, sedimentation, filtration, and disinfection (see :numref:`figure_treatment_train`)."
# translate_text(test_text_01, target_lang='es')
# translate_text(test_text_02, target_lang='es')
# translate_text(test_text_03, target_lang='es')
# translate_text(test_text_04, target_lang='es')
translate_text(test_text_05, target_lang='es')
# translate_text(test_text_06, target_lang='es')
# translate_text(test_text_07, target_lang='es')
# translate_text(test_text_08, target_lang='es')
