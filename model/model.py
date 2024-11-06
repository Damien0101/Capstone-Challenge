import pandas as pd
import unicodedata
import spacy


json_data = pd.read_json('articles.json')

# spacy.cli.download('fr_core_news_sm') to run once to install pckgs
nlp = spacy.load("fr_core_news_sm")


def clean_text(json_data = json_data):
    cpt = 0
    for summary in json_data['summary']:
        print(type(summary))
        cpt += 1
        print(cpt)

print(clean_text())