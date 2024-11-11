import json

with open('data/clean_articles.json', 'r') as f:
    jsons = json.load(f)

titles = [item['title'] for item in jsons]


'''from ..Utils.prepoTitle import titles

t = titles()
print(t)'''