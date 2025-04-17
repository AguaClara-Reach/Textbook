import re

# List of names to exclude (e.g., "AguaClara")
EXCLUDED_NAMES = ["AguaClara"]

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
escaped_names = [re.escape(name) for name in EXCLUDED_NAMES]
name_pattern = "|".join(escaped_names)

# Full combined pattern
full_pattern = f"({base_pattern}|{name_pattern})"

# Compile the regex
combined_regex = re.compile(full_pattern)

def split_text_excluding_patterns(text):
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


# Example usage
text = "Design information for the AguaClara clarifier is available in `the Clarifier Design chapter of The Physics of Water Treatment Design <https://aguaclara.github.io/Textbook/Clarification/Clarifier_Design.html>`_."
print("Original text:", text)
split_parts = split_text_excluding_patterns(text)
print("Recursively split parts:", split_parts)
