import pandas as pd
import streamlit as st
import numpy as np 
import matplotlib.pyplot as plt
from pytrends.request import TrendReq
from bertopic import BERTopic
from datetime import datetime, timedelta
import plotly.express as px

st.title("Trend tracker 📈")
st.markdown("##### Easily discover if a word or phrase is trending with this app. Enter a keyword or sentence and see if it’s gaining popularity. Made for journalists looking to choose articles with current trends, the app provides a visual timeline of the trend’s activity helping you identify the best topics to cover.")

with st.sidebar:
    st.title('title')

pytrends = TrendReq(hl='fr-FR', tz=360)
user_input = st.text_input(label='**Enter a word/sentence**')

if user_input:
    pytrends.build_payload([user_input], cat=0, timeframe='today 3-m', geo='BE')
    trend_data = pytrends.interest_over_time()
    
    three_months_ago = datetime.now() - timedelta(days=90)
    trend_data = trend_data[trend_data.index > three_months_ago]

    dates = trend_data.index.to_list()
    day_month = [date.strftime('%m-%d') for date in dates]
    new_date = [f'{date[3:]} - {date[:2]}' for date in day_month]


    keyword_trend_list = trend_data[trend_data.columns[0]].tolist()
    
    data_lst = [new_date, keyword_trend_list]

    df = pd.DataFrame(data_lst).transpose()
    df.columns = ['Date (day - month)', 'Value (%)']

    fig = px.area(df, x="Date (day - month)", y="Value (%)", color="Value (%)", line_group="Value (%)")
    fig.update_layout(title=f'Trend of "{user_input}" over the last 3 months', xaxis_tickangle=-45, width=1000, height=500)

    st.plotly_chart(fig)
    
    max_value_date = df.loc[df['Value (%)'].idxmax(), 'Date (day - month)']
    st.markdown(f'#### The date where there is the highest value is: {max_value_date} 💡')