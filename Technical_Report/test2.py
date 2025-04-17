from googletrans import Translator

def test_translator_behavior(text, target_lang='es'):
    translator = Translator()

    # Print the original text to debug
    print(f"Original text: '{text}'")

    try:
        # Remove the `***` symbols if they exist before translating
        stripped_text = text.strip('*') if text.startswith('***') and text.endswith('**') else text

        # Translate using the translator
        translated = translator.translate(stripped_text, dest=target_lang).text.strip()  # Strip leading/trailing spaces

        # Re-add the `***` symbols around the translated text if needed
        if text.startswith('**') and text.endswith('**'):
            translated = f"**{translated}**"  # Keep the *** around it without adding extra spaces
        elif text.startswith('**'):
            translated = f"**{translated}"  # Add opening *** if it's missing
        elif text.endswith('**'):
            translated = f"{translated}**"  # Add closing *** if it's missing

        # Print the translated text to see any issues
        print(f"Translated text: '{translated}'")
        
        return translated

    except Exception as e:
        print(f"Error during translation: {e}")
        return text

# Test cases with different input styles
test_translator_behavior("diffuser", target_lang='es')
