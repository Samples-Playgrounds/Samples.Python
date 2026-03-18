

```python
stop_words = set(nltk.corpus.stopwords.words("english"))
for key, value in data.iteritems():
    print type(value), value
    tokenized_article = nltk.word_tokenize(value.lower())
    print tokenized_article
    break
```

*   https://www.scaler.com/topics/nlp/nltk-in-nlp-python/

*   https://blog.gopenai.com/natural-language-processing-nlp-with-pythons-nltk-package-abcc60f9464b

*   https://medium.com/@danielwume/getting-started-with-nltk-10-essential-examples-for-natural-language-processing-in-python-54451eae1366

*   https://stackoverflow.com/questions/40893874/encoding-issue-using-nltk

*   https://stackoverflow.com/questions/46203023/how-can-i-make-my-python-nltk-pre-processing-code-more-efficient

*   https://guides.library.upenn.edu/penntdm/python/nltk

*   Python NLTK Tutorial 1 - Getting started with NLTK

    *   https://www.youtube.com/watch?v=LQQbW3Pve5U

```python
#Variable Initialization

text = """
In the face of changing market conditions and pressure to accelerate growth, the ability for customers to do more 
with less is critical. And while the cloud has long been the north star for realizing efficiencies and accelerating 
innovation, at Microsoft, we understand that these benefits also need to happen outside of the cloud. In 2021 we 
announced the general availability of Azure Arc-enabled SQL Managed Instance. Previously only available in Azure, 
Azure Arc-enabled SQL Managed Instance allows customers to build new cloud native applications on any infrastructure, 
in their on-premises environments and across other public clouds. Now, we are offering a way for customers to make the 
most of their legacy applications, with Azure Arc-enabled SQL Server.
"""

text.encode('ascii', errors='replace') #Encode and remove any special characters.

# STEP 1 : Tokenize the text. Tokenizing the text by sentence gives us list of strings that are sentences.
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation

import nltk
nltk.download('punkt')       
sents = sent_tokenize(text)
sents
word_sent = word_tokenize(text.lower())
word_sent



# STEP 2: Remove stop words to filter from the text

import nltk;
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
stop_words 


# Make a list of words that are not stop words.
filtered_list = []
filtered_list=[word for word in word_sent if word not in stop_words]
word_sent


# STEP 3: Construct frequency distribution of words. It has the words (Key) in one column and number 
# of occurrences (Value) in other. The higher the frequency, the more important the word is considered.

from nltk.probability import FreqDist
freq = FreqDist(word_sent)
freq


# STEP 4: Find most frequent word

from heapq import nlargest
nlargest(3, freq, key=freq.get)


# STEP 5: Create dictionary with sentences and significant scores.

from collections import defaultdict
ranking = defaultdict(int)
for i, sent in enumerate(sents):
    for w in word_tokenize(sent.lower()):
        if w in freq:
            ranking[i] += freq[w]            
ranking

#Pick top one sentence based on the significant score
#This will return our summarized output in single sentence.

sents_idx = nlargest(1, ranking, key=ranking.get)
sents_idx

[sents[j] for j in sorted(sents_idx)]
```

*   https://gist.github.com/leebird/48dee4b1237c7f35781915144599a848


```python
import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize

text = "This is an example sentence, showing off the tokenization process."

tokens = word_tokenize(text)

print(tokens)

# ['This', 'is', 'an', 'example', 'sentence', ',', 'showing', 'off', 'the', 'tokenization', 'process', '.']

print(120*"=")

# Variable Initialization

text = """
In the face of changing market conditions and pressure to accelerate growth, the ability for customers to do more 
with less is critical. And while the cloud has long been the north star for realizing efficiencies and accelerating 
innovation, at Microsoft, we understand that these benefits also need to happen outside of the cloud. In 2021 we 
announced the general availability of Azure Arc-enabled SQL Managed Instance. Previously only available in Azure, 
Azure Arc-enabled SQL Managed Instance allows customers to build new cloud native applications on any infrastructure, 
in their on-premises environments and across other public clouds. Now, we are offering a way for customers to make the 
most of their legacy applications, with Azure Arc-enabled SQL Server.
"""

text.encode('ascii', errors='replace') #Encode and remove any special characters.

# STEP 1 : Tokenize the text. Tokenizing the text by sentence gives us list of strings that are sentences.
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation

import nltk
nltk.download('punkt')       
sents = sent_tokenize(text)
sents
word_sent = word_tokenize(text.lower())
word_sent



# STEP 2: Remove stop words to filter from the text

import nltk;
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
stop_words 


# Make a list of words that are not stop words.
filtered_list = []
filtered_list=[word for word in word_sent if word not in stop_words]
word_sent


# STEP 3: Construct frequency distribution of words. It has the words (Key) in one column and number 
# of occurrences (Value) in other. The higher the frequency, the more important the word is considered.

from nltk.probability import FreqDist
freq = FreqDist(word_sent)
freq


# STEP 4: Find most frequent word

from heapq import nlargest
nlargest(3, freq, key=freq.get)


# STEP 5: Create dictionary with sentences and significant scores.

from collections import defaultdict
ranking = defaultdict(int)
for i, sent in enumerate(sents):
    for w in word_tokenize(sent.lower()):
        if w in freq:
            ranking[i] += freq[w]            
ranking

#Pick top one sentence based on the significant score
#This will return our summarized output in single sentence.

sents_idx = nlargest(1, ranking, key=ranking.get)
sents_idx

[sents[j] for j in sorted(sents_idx)]
```