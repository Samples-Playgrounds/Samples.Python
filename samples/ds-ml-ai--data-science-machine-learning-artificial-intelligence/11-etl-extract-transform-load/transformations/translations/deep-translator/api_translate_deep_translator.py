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

def translate_text (text: str, lang_destination: str, translator: str) -> str:
    """
    Translate the text using the specified translator and target language.    
    """
    
    lines = text.splitlines(keepends=True)
    translation_lines = []

    i = 1

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
        i += 1

    translation = ''.join(translation_lines)

    return translation

def translate_file                      (
                                         source: str,
                                         lang_destination: str, 
                                         translator: str, 
                                         api_key: str = None
                                         ) -> str:
    """
    Translate the content of a text file using the specified translator and target language.    
    """
    with open(source, 'r') as file:
        content = file.read()
    return translate_text(content, lang_destination, translator)