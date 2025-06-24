import translators as ts


def translate_text (source: str, lang_destination: str, translator: str) -> str:


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

        print(f"Translating line    : {line}")
        translation_line = ts.translate_text(line, to_language=lang_destination, translator=translator)
    
        translation_lines.append(translation_line)
        print(f"Translated line     : {translation_line}")

    
    translation = ''.join(translation_lines)

    return translation
