import streamlit as st
import numpy as np 
import matplotlib.pyplot as plt
from pytrends.request import TrendReq
from bertopic import BERTopic


st.title("Trend tracker")
st.markdown("Easily discover if a word or phrase is trending with this app. Enter a keyword or sentence and instantly see if it’s gaining popularity. Made for journalists looking to choose articles with current trends, the app provides a visual timeline of the trend’s activity helping you identify the best topics to cover.")

st.sidebar.title("sidebar")

pytrends = TrendReq(hl='fr-FR', tz=360)
user_input = st.text_input(label='Enter a word/sentence')

if user_input:
    pytrends.build_payload([user_input], cat=0, timeframe='today 3-m', geo='BE')
    trend_data = pytrends.interest_over_time()
    st.write(trend_data)

# plt.plot(x, y)
# st.pyplot(plt)
