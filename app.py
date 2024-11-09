import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Trend tracker")
st.markdown("Easily discover if a word or phrase is trending with this app! Enter a keyword or sentence, and instantly see if it’s gaining popularity. Perfect for journalists looking to align articles with current trends, the app provides a visual timeline of the trend’s activity, helping you identify the best topics to cover.")

st.sidebar.title("sidebar")
user_input = st.sidebar.text_input("Entre a word or a sentence..", "")

if user_input:
    st.write(f"**You entered:** {user_input}")
st.subheader("Calculated Result")

# plt.plot(x, y)
# st.pyplot(plt)

