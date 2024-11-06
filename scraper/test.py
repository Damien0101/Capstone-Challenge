from pytrends.request import TrendReq
from bertopic import BERTopic


pytrends = TrendReq(hl='fr-FR', tz=360)

keywords = ["deadpool"]
pytrends.build_payload(keywords, cat=0, timeframe='today 12-m')


trend_data = pytrends.interest_over_time()

print(trend_data)

articles = [
    "L'IA progresse dans le domaine médical...",
    "L'IA et la robotique deviennent de plus en plus populaires...",
    "De nombreuses industries adoptent l'IA..."
]

topic_model = BERTopic()
topics, _ = topic_model.fit_transform(articles)

topic_model.visualize_topics_over_time()

