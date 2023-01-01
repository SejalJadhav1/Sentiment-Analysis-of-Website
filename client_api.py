import numpy as np
import pandas as pd
import bs4
import nltk
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')
nltk.download('vader_lexicon')
from bs4 import BeautifulSoup as bs
import requests
from requests.exceptions import MissingSchema
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


def retrieve_data(fill_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0', }
    data = [fill_url]

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
    key = [] 
    value = []
    for i in final_dict.keys():
        key.append(i)
    for i in final_dict.values():
        value.append(i)
    return key , value

score = retrieve_data(fill_url)

left_column, middle_column, right_column  = st.columns(3)
with left_column:
        st.subheader("Negative-Score:")
        st.subheader(score[1][0])
with middle_column:
        st.subheader("Neutral-Score:")
        st.subheader(score[1][1])
with right_column:
        st.subheader("Positive-Score:")
        st.subheader(score[1][2])

st.markdown("""---""")

def pos_neg_neu(sentiment_text):
        if (score[1][0] >= score[1][1]) and (score[1][2] >= score[1][0]):
            return "The sentiment of your input website is 'NEGATIVE'"
        elif (score[1][1] >= score[1][2]) and (score[1][1] >= score[1][0]):
            return "The sentiment of your input website is 'NEUTRAL'"
        else:
            return "The sentiment of your input website is 'POSITIVE'"


st.subheader(pos_neg_neu(score))

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

    
