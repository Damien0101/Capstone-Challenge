import json

with open('data/clean_articles.json', 'r') as f:
    jsons = json.load(f)

titles = [item['title'] for item in jsons]

with open('data/titles.txt', 'w', encoding='utf-8') as file:
    for title in titles:
        file.write(title + '\n')