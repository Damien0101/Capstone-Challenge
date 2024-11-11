from pytrends.request import TrendReq
from bertopic import BERTopic
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

keywords = ["Donald Trump"]

pytrends = TrendReq(hl='fr-FR', tz=360)

pytrends.build_payload(keywords, cat=0, timeframe='today 12-m', geo='BE')
trend_data = pytrends.interest_over_time()

print(trend_data)

three_months_ago = datetime.now() - timedelta(days=90)
trend_data = trend_data[trend_data.index > three_months_ago]

dates = trend_data.index.to_list()
day_month = [date.strftime('%m-%d') for date in dates]

keyword_trend_list = trend_data[trend_data.columns[0]].tolist()

