
import api

# document per local path or URL
texts = [
   "This is the text I would like to chunk up. It is the example text for this exercise",

]
#  "/Volumes/FAT_VERB/learning/books/topics/microsoft/architecture/adevelopersguidetonetinazure.pdf"
#   "https://arxiv.org/pdf/2408.09869"


for text in texts:
      chunks = api.split_on_character(text, 35)
      for i, chunk in enumerate(chunks):
          print(f"Chunk {i}: {chunk}")
