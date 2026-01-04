# Translations

readme.md

*   https://pypi.org/project/translate/


    ```shell
    pip install translate
    ```

https://github.com/terryyin/translate-python

https://lokalise.com/blog/how-to-translate-languages-in-python-with-google-translate-and-deepl-plus-more/

https://pypi.org/project/deep-translator/

    ```shell
    pip install deep-translator
    ```

https://github.com/nidhaloff/deep-translator

https://medium.com/analytics-vidhya/how-to-translate-text-with-python-9d203139dcf5

https://cloud.google.com/translate/docs/reference/libraries/v2/python

    ```shell
    pip install google-cloud-translate
    ```

https://cloud.google.com/translate/docs/reference/libraries/v2/csharp

https://github.com/DeepLcom/deepl-python

https://github.com/argosopentech/argos-translate

    ```shell
    pip install argostranslate
    ```

*   https://thepythoncode.com/article/translate-text-in-python


## Diverse

*   https://lokalise.com/blog/how-to-translate-languages-in-python-with-google-translate-and-deepl-plus-more/


translations

https://www.reddit.com/r/LocalLLaMA/comments/1iln1lj/good_local_llm_for_text_translation/

This is what I found for free models specifically targeted at translation:

NLLB-200-distilled-1.3B (proprietary license may be a problem)

OPUS-MT (Apache 2.0 license)

MADLAD-400 (Apache 2.0 license)

Despite the above tools being targeted specifically at translation, I found their performance to be mediocre. Surprisingly I had much better results with these general text-generation instruction-oriented models:

deepseek-r1:14b (MIT license)

huihui_ai/qwen2.5-1m-abliterated:14b (Apache 2.0 license)

Mistral-Small-24B-Instruct-2501-GGUF:Q8_0 (Apache 2.0 license)

gemma2 (weird license but allows most use cases)

Qwen2.5:0.5B-instruct-q8 Qwen2.5:1.5B-instruct-q8

Tower instruct on hugging face is specifically targeted for translation, it is only 10-14B I think

Mistral is a good option for multilingual local translation


https://www.reddit.com/r/LocalLLaMA/comments/1929h6p/local_translationfocused_models_and_how_do_you/

ALMA-13B is specifically for translation. I've downloaded it but not tried it yet.

My usual go-to for translation is PuddleJumper-13B-v2. I prompt it with the format Translate this English to German: "..." and that mostly works well, except that it frequently leads or trails inference 

Seamless-M4T or MADLAD-400

https://www.reddit.com/r/LocalLLaMA/comments/1dc2xur/best_llm_for_translating_texts/

Gemma 2 and EuroLLM is the best for me, but strangely Gemma 2 is better at translating from a non-English language into English and EuroLLM is better at translating from English into a non-English language.

Aya 23, Mixtral and Llama 3 are the usual suspects, but please surprise me.

NLLB

owever, there's a CTranslate2 version. It should run reasonably fast https://huggingface.co/OpenNMT/nllb-200-distilled-1.3B-ct2-int8

Phi3-medium translates better than small aya23. Qwen2 also provides good translation, but sometimes suddenly changes output to Chinese. Check lmsys leaderboard for category by language you interested in.

Cat-Llama-3-70B-instruct for translation. I always use 3 offline models + Google translate to translate Chinese to English, and Llama3-70B is on par with Google Translate. Llama-3-8b is also good but not as good as the 70B.

https://medium.com/@svosh2/how-i-built-rag-application-that-assists-me-to-learn-croatian-410f86f80775