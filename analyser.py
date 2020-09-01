#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pickle
import numpy as np
import pandas as pd


# In[2]:


model=pickle.load(open("model.pkl","rb"))


# In[3]:


def predict_sentiment(text):
    
    input=text
    pred=model.score(input)
    if pred>0:
        return "Positive Sentiment"
    elif pred<0:
        return "Negative Sentiment"
    else:
        return "Neutral Sentiment"
        


# In[4]:


def main():
    st.title("Sentiment Analyser On IMDB")
    text=st.text_input("Text")
    
    
    if st.button("Predict"):
        output=predict_sentiment(text)
        st.success("The Given Sentiment is {}".format(output))
        
   


# In[5]:


if __name__=="__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:




