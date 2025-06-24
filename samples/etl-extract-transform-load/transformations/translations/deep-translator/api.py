from deep_translator import (GoogleTranslator,
                             ChatGptTranslator,
                             MicrosoftTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             PapagoTranslator,
                             DeeplTranslator,
                             QcriTranslator,
                             single_detection,
                             batch_detection)

def translate_text (source: str, lang_destination: str, translator: str) -> str:

    with open(source, 'r') as file:
        lines = []
        for line in file:   
            lines.append(line)

    translation_lines = []
    for line in lines:
        # Skip empty lines - do not translate them
        if not line.strip():
            translation_lines.append(line)
            continue

        match translator.lower():
            case "google":
                translation_line = GoogleTranslator(source='auto', target=lang_destination).translate(line)
            case "chatgpt":
                translation_line = ChatGptTranslator(source='auto', target=lang_destination).translate(line)
            case "microsoft":
                translation_line = MicrosoftTranslator(source='auto', target=lang_destination).translate(line)
            case "pons":
                translation_line = PonsTranslator(source='auto', target=lang_destination).translate(line)
            case "linguee":
                translation_line = LingueeTranslator(source='auto', target=lang_destination).translate(line)
            case "mymemory":
                translation_line = MyMemoryTranslator(source='auto', target=lang_destination).translate(line)
            case "yandex":
                translation_line = YandexTranslator(source='auto', target=lang_destination).translate(line)
            case "papago":
                translation_line = PapagoTranslator(source='auto', target=lang_destination).translate(line)
            case "deepl":
                translation_line = DeeplTranslator(source='auto', target=lang_destination).translate(line)
            case "qcri":
                translation_line = QcriTranslator(source='auto', target=lang_destination).translate(line)
            case _: # default:
                translation_line = GoogleTranslator(source='auto', target=lang_destination).translate(line)
        
        
        translation_lines.append(translation_line)

        print(f"Translating line    : {line}")
        print(f"Translated line     : {translation_line}")


    translation = ''.join(translation_lines)

    return translation
