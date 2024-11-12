from pytrends.request import TrendReq
from bertopic import BERTopic
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

keywords = ["Donald Trump"]

# Set up a session with retries and backoff
session = requests.Session()
retries = Retry(
    total=5,  # Total number of retries
    backoff_factor=0.1,  # Backoff factor to apply between attempts
    status_forcelist=[429, 500, 502, 503, 504],  # Retry on these HTTP status codes
    allowed_methods=["GET", "POST"]  # Retry for these methods
)
adapter = HTTPAdapter(max_retries=retries)
session.mount("https://", adapter)
session.mount("http://", adapter)

# Configure pytrends to use the session with retries
pytrends = TrendReq(hl='fr-FR', tz=360, requests_args={'verify': False})

# Build payload and get interest over time data
pytrends.build_payload(keywords, cat=0, timeframe='today 12-m', geo='BE')
trend_data = pytrends.interest_over_time()

print(trend_data)

three_months_ago = datetime.now() - timedelta(days=90)
trend_data = trend_data[trend_data.index > three_months_ago]

dates = trend_data.index.to_list()
day_month = [date.strftime('%m-%d') for date in dates]

keyword_trend_list = trend_data[trend_data.columns[0]].tolist()
