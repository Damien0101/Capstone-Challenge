import json

def titles():
    with open('data/clean_articles.json', 'r') as f:
        jsons = json.load(f)

    articles = []


    for article in jsons:
        for k, v in article.items():
            articles.append(v if k == 'title' else '')

    all_articles = [a for a in articles if a != '']     
    return all_articles

