from pytrends.request import TrendReq
from bertopic import BERTopic


pytrends = TrendReq(hl='fr-FR', tz=360)

keywords = ["Trump"]
pytrends.build_payload(keywords, cat=0, timeframe='today 12-m')


trend_data = pytrends.interest_over_time()

print(trend_data, type(trend_data))

