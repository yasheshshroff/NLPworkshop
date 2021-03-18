#!/usr/bin/env python
# coding: utf-8

# ## Disaster or not: Text Classification using TFIDF and Logistic Regression

# In[ ]:


# get_ipython().system('wget https://github.com/ravi-ilango/acm-dec-2020-nlp/blob/main/lab2/disaster_data.zip?raw=true -O disaster_data.zip')
    
# get_ipython().system('unzip disaster_data.zip')


# In[ ]:


import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
# get_ipython().run_line_magic('matplotlib', 'inline')


# ### Load data

# In[ ]:


pd.read_csv('./disaster_data/train.csv').head()


# In[ ]:


#
# queries are stored in the variable query_text
# correct intent labels are stored in the variable labels
#
query_text = pd.read_csv('./disaster_data/train.csv').text.values
labels = pd.read_csv('./disaster_data/train.csv').target.values

query_text.shape


# In[ ]:


plt.hist(labels)
plt.xlabel('target')
plt.ylabel('count')
plt.title('target distribution')
plt.xticks(np.arange(len(np.unique(labels))));


# ### Train and Test split

# In[ ]:


from sklearn.model_selection import train_test_split

query_train, query_test, y_train, y_test = train_test_split(query_text, labels, test_size=0.2, random_state=13)


# ### Vectorize the text document

# In[ ]:


from sklearn.feature_extraction.text import TfidfVectorizer

ngram_range = (1,2)

vectorizer = TfidfVectorizer(ngram_range=ngram_range, 
                             stop_words='english', 
                             max_features=150)

X_train = vectorizer.fit_transform(query_train).toarray()
X_test = vectorizer.transform(query_test).toarray()


# In[ ]:





# ### Fit a classifier using the vectors

# In[ ]:


from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()
clf.fit(X_train, y_train)

with open('vectorizer.pk', 'wb') as fin: 
    pickle.dump(vectorizer, fin)

with open('clf.pk', 'wb') as fin: 
    pickle.dump(clf, fin)




# ### Calculate Test Accuracy

# In[ ]:


y_pred = clf.predict(X_test)
# print (f"Test Accuracy = {(y_pred == y_test).mean()}")


# ### Check Model Prediction

# In[ ]:


def predict(model, query_txt):
    x = vectorizer.transform([query_txt]).toarray()
    pred = model.predict(x)
    if pred[0] == 1:
        print ("Disaster")
    else:
        print ("Not a disaster")


# In[ ]:


# predict (clf, "Forest fire near La Ronge Sask. Canada")


# In[ ]:


# predict(clf, "The weather is awesome")


# In[ ]:




