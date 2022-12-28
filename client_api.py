import numpy as np
import pandas as pd
import bs4
import nltk
nltk.download('stopwords')
from bs4 import BeautifulSoup as bs
import requests
from requests.exceptions import MissingSchema
import html5lib
import json
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


def _load_url_or_file(self, url):
        try:
            response = requests.get(url)
            if response.ok:
                return response.text
            else:
                raise requests.HTTPError
        except (MissingSchema, requests.HTTPError):
            st.write("tryyy")

 st.write(_load_url_or_file(fill_url))           
            



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

    
