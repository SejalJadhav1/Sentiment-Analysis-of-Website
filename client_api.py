import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import html5lib
from urllib.request import urlopen
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
import streamlit as st
import string
from collections import Counter
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

st.set_page_config(page_title="Sentiment Analysis of Website", page_icon=":memo::", layout="wide")

st.title(":memo: Sentiment Analysis of Website")
st.markdown("##")


# st.write("Fill in below")

fill_url = st.text_input("Enter the website (url) you want your sentiment scores for :")

# st.warning("Make sure your url begins with http")

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
    loweralphabets = "abcdefghijklmnopqrstuvwxyz"
    upperalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    x = loweralphabets + upperalphabets
    res = []
    for i in test_list:
        a = ""
        for j in i:
            if j in x:
                a += j
        res.append(a)
    for i in res:
        if i == "":
            res.remove(i)
    filtered_words = [word for word in res if word not in stopwords.words('english')]

    lemmatizer = WordNetLemmatizer()
    lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in filtered_words])

    # word_list = nltk.word_tokenize(lemmatized_output)

    score = SentimentIntensityAnalyzer().polarity_scores(lemmatized_output)
    new_keys = ['negative-score', 'neutral-score', 'positive-score', 'compound']
    final_dict = dict(zip(new_keys, list(score.values())))

    return final_dict, lemmatized_output


score = retrieve_data(fill_url)[0]

left_column, middle_column, right_column  = st.columns(3)
with left_column:
    st.subheader("Negative-Score:")
    st.subheader(score["negative-score"])
with middle_column:
    st.subheader("Neutral-Score:")
    st.subheader(score["neutral-score"])
with right_column:
    st.subheader("Positive-Score:")
    st.subheader(score["positive-score"])

st.markdown("""---""")


def pos_neg_neu(sentiment_text):
    if (score['negative-score'] >= score['neutral-score']) and (score['negative-score'] >= score['positive-score']):
        return "The sentiment of your input website is 'NEGATIVE'"
    elif (score['neutral-score'] >= score['negative-score']) and (score['neutral-score'] >= score['positive-score']):
        return "The sentiment of your input website is 'NEUTRAL'"
    else:
        return "The sentiment of your input website is 'POSITIVE'"


st.subheader(pos_neg_neu(score))


# st.error("Error")

# st.exception("exception")


# st.help(help)


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