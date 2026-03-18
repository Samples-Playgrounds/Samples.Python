import nltk

nltk.download('punkt')
nltk.download('stopwords')

def tokens_in_text (
                        text: str,
                    ) -> tuple[ list[int], int, list[str] ]:
    """
    """
    from nltk.tokenize import word_tokenize

    tokens = word_tokenize(text)
    count_tokens = len(tokens)

    return tokens, count_tokens


def sentences_in_text (
                        text: str,
                    ) -> tuple[ list[int], int, list[str] ]:
    """
    """
    text.encode('ascii', errors='replace') #Encode and remove any special characters.

    # STEP 1 : Tokenize the text. Tokenizing the text by sentence gives us list of strings that are sentences.
    from nltk.tokenize import sent_tokenize, word_tokenize
    from nltk.corpus import stopwords
    from string import punctuation

    sents = sent_tokenize(text)
    sents
    word_sent = word_tokenize(text.lower())
    word_sent

    # STEP 2: Remove stop words to filter from the text

    import nltk;
    stop_words = set(stopwords.words('english'))
    stop_words 

    # Make a list of words that are not stop words.
    filtered_list = []
    filtered_list=[word for word in word_sent if word not in stop_words]
    word_sent

    return sents, stop_words, filtered_list    