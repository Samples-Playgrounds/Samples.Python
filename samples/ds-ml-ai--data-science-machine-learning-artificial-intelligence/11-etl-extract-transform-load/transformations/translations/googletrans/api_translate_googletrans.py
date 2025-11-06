from googletrans import Translator


def translate_text (source: str, lang_destination: str) -> str:

    translator = Translator()

    with open(source, 'r') as file:
        lines = []
        for line in file:   
            lines.append(line)

    translation_lines = []
    for line in lines:
        translation_lines.append(line)
        # Skip empty lines - do not translate them
        if not line.strip():
            continue

        translation_line = translator.translate(line, dest=lang_destination)    
        translation_lines.append(translation_line)

        print(f"Translating line    : {line}")
        print(f"Translated line     : {translation_line}")


    translation = ''.join(translation_lines)

    return translation
