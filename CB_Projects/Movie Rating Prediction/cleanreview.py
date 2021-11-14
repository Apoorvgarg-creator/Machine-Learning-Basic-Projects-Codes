#!/usr/bin/env python
# coding: utf-8

# #### Create a NLP pipeline to 'clean' Reviews Data
# - Load input File and read reviews
# - Tokenise
# - Remove stopwrods
# - perform Stemming
# - Write cleaned data to output file

# In[17]:


import sys
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import EnglishStemmer
from nltk.corpus import stopwords


# In[18]:


tokenizer = RegexpTokenizer(r'\w+')
en_stopwords = set(stopwords.words('english'))
ps = EnglishStemmer()


# In[19]:


def getcleanRev(review):

    review = review.lower()
    # review = review.replace("<br /><br />"," ")

    # RegexpTokenizer
    tokens = tokenizer.tokenize(review)
    new_tokens = [ token for token in tokens if token not in en_stopwords]
    stemmed_tokens = [ps.stem(token) for token in new_tokens]

    clean_review = ' '.join(stemmed_tokens)

    return clean_review


# In[20]:


sample_text = "mature intelligent and highly charged melodrama unbelivebly filmed in China in 1948. wei wei's stunning performance as the catylast in a love triangle is simply stunning if you have the oppurunity to see this magnificent film take it,pos"


# In[21]:


print(getcleanRev(sample_text))
