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
    st.title('⚙️ Settings')
    st.sidebar.write("**Tip**: Try shorter date ranges to focus on recent changes in trends.")

    start = st.date_input('start date')
    end = st.date_input('end date')


pytrends = TrendReq(hl='fr-FR', tz=360)
user_input = st.text_input(label='**Enter a word/sentence**')

if user_input:
    if start and end:
        timeframe = f'{start.strftime("%Y-%m-%d")} {end.strftime("%Y-%m-%d")}'
        pytrends.build_payload([user_input], cat=0, timeframe=timeframe, geo='BE')
        trend_data = pytrends.interest_over_time()

        if not trend_data.empty:
            dates = trend_data.index.to_list()
            formatted_dates = [date.strftime('%d - %m - %y') for date in dates]

            keyword_trend_list = trend_data[trend_data.columns[0]].tolist()

            data_lst = [formatted_dates, keyword_trend_list]

            df = pd.DataFrame(data_lst).transpose()
            df.columns = ['Date', 'Value (%)']

            fig = px.area(df, x="Date", y="Value (%)")
            fig.update_layout(title=f'Trend of "{user_input}" from {start.strftime('%d/%m/%y')} to {end.strftime('%d/%m/%y')}', xaxis_tickangle=-45, width=1000, height=500)
            fig.update_xaxes(nticks=15)
            st.plotly_chart(fig)

            max_value_date = df.loc[df['Value (%)'].idxmax(), 'Date']
            st.markdown(f'#### The date where the highest value is: {max_value_date} 💡')
