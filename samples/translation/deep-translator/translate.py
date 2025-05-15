from deep_translator import GoogleTranslator
from deep_translator import PonsTranslator
from deep_translator import MicrosoftTranslator
from deep_translator import LingueeTranslator
from deep_translator import MyMemoryTranslator

text_en = "keep it up, you are awesome"


# Use any translator

translated = GoogleTranslator(source='auto', target='de').translate(text_en)  
# output -> Weiter so, du bist großartig
print(f"GoogleTranslator                = {translated}")


translated = LingueeTranslator(source='auto', target='german').translate(text_en)  
# output -> Weiter so, du bist großartig
print(f"LingueeTranslator               = {translated}")

#translated = MyMemoryTranslator(source='en', target='de').translate(text_en)  
# output -> Weiter so, du bist großartig
#print(f"MyMemoryTranslator              = {translated}")

# translated = MicrosoftTranslator(source='auto', target='de').translate(text_en)  
# output -> Weiter so, du bist großartig
# print(f"MicrosoftTranslator = {translated}")

translated = PonsTranslator(source='english', target='german').translate(text_en)  
# output -> Weiter so, du bist großartig
print(f"PonsTranslator = {translated}")

#                             ChatGptTranslator,
#                             ,
#                             ,
#                             YandexTranslator,
#                             PapagoTranslator,
#                             DeeplTranslator,
#                             QcriTranslator,
