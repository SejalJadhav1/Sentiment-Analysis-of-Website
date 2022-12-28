import numpy as np
import pandas as pd
import bs4
from bs4 import BeautifulSoup as bs
import requests
import html5lib
from urllib.request import urlopen
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import streamlit as st
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

st.set_page_config(page_title="Sentiment Analysis of Website", page_icon=":memo::", layout="wide")

st.title(":memo: Sentiment Analysis of Website")
st.markdown("##")



fill_url = st.text_input("Enter the website (url) you want your sentiment scores for :")

def retrieve_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0', }
    data = [url]

    for i in data:
        r = requests.get(i, headers=headers)
        htmlcontent = r.content

        soup = bs(htmlcontent, "html.parser")
        title = soup.title
        
        list_ = []
        list_.append(title.get_text())
        
        for data in soup.find_all("p"):
            list_.append(data.get_text()) 

        l = []
        for i in list_:
            i = i.split(" ")
            l = l + i 

    test_list = l
    loweralphabets="abcdefghijklmnopqrstuvwxyz"
    upperalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    x=loweralphabets+upperalphabets
    res=[]
    for i in test_list:
        a = ""
        for j in i:
            if j in x:
                a+=j
        res.append(a)
    for i in res:
        if i=="":
            res.remove(i)
            
    stop_words = set(stopwords.words('english'))        
    filtered_words = [w for w in res if not w.lower() in stop_words]

    lemmatizer = WordNetLemmatizer()
    lemmatized_output = ' '.join([lemmatizer.lemmatize(i) for i in filtered_words])

    #word_list = nltk.word_tokenize(lemmatized_output)
    
    score = SentimentIntensityAnalyzer().polarity_scores(lemmatized_output)
    new_keys = ['negative-score', 'neutral-score', 'positive-score', 'compound']
    final_dict = dict(zip(new_keys, list(score.values())))
        
    return final_dict

st.write(retrieve_data(fill_url))


if st.checkbox("Show/Hide"):
    st.write("If you like my work, and have any suggetions, mail me on sejalsj2001@gmail.com")

hide_st_style = """
             <style>
             #MainMenu {visibility: hidden;}
             footer {visibility: hidden;}
             header {visibility: hidden;}
             </style>
             """
st.markdown(hide_st_style, unsafe_allow_html=True)

    
