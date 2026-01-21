2. Context Window & Memory Test

To verify if the model actually supports a long context window without forgetting information, you 
can test it with a needle-in-a-haystack prompt: 

I will provide you with a very long document [or many files]. Please analyze this information and 
tell me:

What is the total word count?
What specific keyword or detail appears only in the middle of the document? [Insert a unique phrase 
like 'Project Sunflower' in the middle of a large text].

Summarize the content from the beginning, middle, and end to prove you haven't lost context.
