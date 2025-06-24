import translate

from translate import Translator

def translate_text (source: str, lang_destination: str) -> str:

    translator = Translator(to_lang=lang_destination)

    with open(source, 'r') as file:
        file_contents = file.read()
 
    translation = translator.translate(file_contents)

    print(translation)
    
    return translation
