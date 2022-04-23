#!/usr/bin/env python
# coding: utf-8

# ## About SpaCy
# 
# - Designed by [Explosion.ai](Explosion.ai) to scale well with 100sk of documents 
# - Excellent framework that allows for custom training relatively easily
# 

# In[ ]:

#get_ipython().run_line_magic('sh', '')
# Installing
#pip install -U pip setuptools wheel
#pip install -U spacy
#python -m spacy download en_core_web_sm


# ### Spacy containers ()
# 
# - [Doc](https://spacy.io/api/doc)
# - [DocBin](https://spacy.io/api/docbin)
# - Example
# - Language
# - Lexeme
# - Span
# - SpanGroup
# - Token

# We will work through examples. Let's load up a model and create a doc object using sample text. 

# In[ ]:


import spacy
nlp = spacy.load("en-core-web-sm")


# In[ ]:


with open("data/nasa.txt", "r") as f:
    text = f.read()

print(text)


# In[ ]:


doc = nlp(text)
print(doc)

# 
