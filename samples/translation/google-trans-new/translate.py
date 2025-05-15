from google_trans_new import google_translator  

text_en = "keep it up, you are awesome"

translator = google_translator()  
translate_text = translator.translate(text_en,lang_tgt='de')
print(translate_text)
print(f"google_translator               = {translate_text}")

translator = google_translator()  
translate_text = translator.translate('สวัสดีจีน',lang_tgt='en')  
# -> Hello china
print(f"google_translator               = {translate_text}")
