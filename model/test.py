from bertopic import BERTopic


articles = [
    "L'IA progresse dans le domaine médical...",
    "L'IA et la robotique deviennent de plus en plus populaires...",
    "De nombreuses industries adoptent l'IA..."
]

topic_model = BERTopic()
topics, _ = topic_model.fit_transform(articles)

topic_model.visualize_topics_over_time()
