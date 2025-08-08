from google.cloud import translate_v2 as translate


def translate_text (source: str, lang_destination: str) -> str:

    translate_client = translate.Client()

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


    if isinstance(text, bytes):
        text = line.decode("utf-8")
    
        translation_line = translate_client.translate(text, target_language=lang_destination)
        
        translation_lines.append(translation_line)
        print(f"Translated line     : {translation_line}")
    
    translation = ''.join(translation_lines)

    return translation
