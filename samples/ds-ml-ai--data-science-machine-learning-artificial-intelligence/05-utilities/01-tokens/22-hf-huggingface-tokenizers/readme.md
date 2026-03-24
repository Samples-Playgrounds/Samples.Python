

*   https://huggingface.co/docs/transformers/main_classes/tokenizer

*   https://github.com/huggingface/tokenizers

    *   most used

    *   used in

        *   https://github.com/huggingface/transformers

*   https://huggingface.co/docs/tokenizers/quicktour


pip install tokenizers


from tokenizers import Tokenizer
from tokenizers.models import BPE

tokenizer = Tokenizer(BPE())


from tokenizers.pre_tokenizers import Whitespace

tokenizer.pre_tokenizer = Whitespace()



from tokenizers.trainers import BpeTrainer

trainer = BpeTrainer(special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"])
tokenizer.train(files=["wiki.train.raw", "wiki.valid.raw", "wiki.test.raw"], trainer=trainer)



output = tokenizer.encode("Hello, y'all! How are you 😁 ?")
print(output.tokens)
# ["Hello", ",", "y", "'", "all", "!", "How", "are", "you", "[UNK]", "?"]



https://www.youtube.com/watch?v=bWLvGGJLzF8

https://www.youtube.com/watch?v=Cz2nvfK28eI

https://www.youtube.com/watch?v=kxjDOzknSEY

https://mohdmus99.medium.com/hands-on-practice-with-tokenizers-in-llms-using-python-5e9f2ee2402b
