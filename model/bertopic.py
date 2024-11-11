from bertopic import BERTopic


articles = [
    "le domaine médical...",
    "la robotique..."
]

topic_model = BERTopic()
topics, _ = topic_model.fit_transform(articles)

topic_model.visualize_topics_over_time()
