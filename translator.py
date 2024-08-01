# Import necessary libraries
from googletrans import Translator, LANGUAGES

def translate_text(text, src_lang='auto', dest_lang='en'):
    """
    Translate the given text from source language to destination language.

    Parameters:
    - text (str): The text to translate.
    - src_lang (str): The source language code (default is 'auto' for auto-detection).
    - dest_lang (str): The destination language code (default is 'en' for English).

    Returns:
    - str: The translated text.
    """
    translator = Translator()
    try:
        # Translate the text
        translation = translator.translate(text, src=src_lang, dest=dest_lang)
        return translation.text
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    """
    Main function to handle user input and display translated text.
    """
    print("Language Translation Tool")
    print("Available languages:")
    for lang_code, lang_name in LANGUAGES.items():
        print(f"{lang_code}: {lang_name}")
    
    text = input("Enter text to translate: ")
    
    src_lang = input("Enter source language code (default 'auto' for auto-detection): ") or 'auto'
    dest_lang = input("Enter destination language code (default 'en' for English): ") or 'en'
    
    if src_lang not in LANGUAGES and src_lang != 'auto':
        print("Invalid source language code. Using default 'auto' for detection.")
        src_lang = 'auto'
    
    if dest_lang not in LANGUAGES:
        print("Invalid destination language code. Using default 'en' for English.")
        dest_lang = 'en'
    
    # Perform the translation
    translated_text = translate_text(text, src_lang, dest_lang)
    
    # Display the translated text
    print(f"\nTranslated text ({LANGUAGES.get(dest_lang, 'English')}):")
    print(translated_text)

if __name__ == "__main__":
    main()
