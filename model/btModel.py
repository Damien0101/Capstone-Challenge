from bertopic import BERTopic
import json

with open('data/clean_articles.json', 'r') as f:
    jsons = json.load(f)

articles = []

for article in jsons:
    for k, v in article.items():
        articles.append(v if k == 'title' else '')

all_articles = [a for a in articles if a != '']     

topic_model = BERTopic()
topics, probs = topic_model.fit_transform(all_articles)

topic_model = BERTopic()
topics, probs = topic_model.fit_transform(all_articles)

topic_info = topic_model.get_topic_info()

topic_info_filtered = topic_info[topic_info['Topic'] != -1]

most_frequent_topics = topic_info_filtered.sort_values(by='Count', ascending=False)

print("most present topic:")
print(most_frequent_topics.head(1))

most_present_topic_id = most_frequent_topics.iloc[0]['Topic']

most_present_topic = topic_model.get_topic(most_present_topic_id)

print("most present topic")
for term, weight in most_present_topic:
    print(f"{term} ({weight:.4f})")



# 'bertopic doc: https://maartengr.github.io/BERTopic/index.html'