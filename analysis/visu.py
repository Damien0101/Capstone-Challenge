import pandas as pd
import plotly.express as px
from pytrends.request import TrendReq
from bertopic import BERTopic
from datetime import datetime, timedelta
import matplotlib.pyplot as plt


keywords = ["trump"]

pytrends = TrendReq(hl='fr-FR', tz=360)

pytrends.build_payload(keywords, cat=0, timeframe='today 12-m', geo='BE')
trend_data = pytrends.interest_over_time()

three_months_ago = datetime.now() - timedelta(days=90)
trend_data = trend_data[trend_data.index > three_months_ago]

dates = trend_data.index.to_list()
day_month = [date.strftime('%m-%d') for date in dates]

keyword_trend_list = trend_data[trend_data.columns[0]].tolist()

data_lst = [day_month, keyword_trend_list]

df = pd.DataFrame(data_lst).transpose()
df.columns = ['date', 'value (%)']

print(df.head())

fig = px.area(df, x="date", y="value (%)", color="value (%)", line_group="value (%)")
fig.update_layout(title = f'Trend of "{keywords[0]}" Over the Last 3 Months', xaxis_tickangle=-45, width=1000, height=500)
fig.show()
