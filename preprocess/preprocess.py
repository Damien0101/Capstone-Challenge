import pandas as pd
import unicodedata
import spacy
import json


def clean_text(text, nlp = spacy.load("fr_core_news_sm")):
    # spacy.cli.download('fr_core_news_sm') to run once to install pckgs
    text = text.replace("'", " ")    
    
    doc = nlp(text)

    cleaned_tokens = [
        token.text for token in doc 
        if not token.is_punct           
        and not token.is_digit        
        and not token.is_space          
        and token.is_alpha               
    ]
    cleaned_text = " ".join(cleaned_tokens)
    return cleaned_text


def remove_accents(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')


def apply_func(json_data):
    articles_list=[]
    for index, row in json_data.iterrows():
        dic = {
            'label': clean_text(remove_accents(row['label'])),
            'title': clean_text(remove_accents(row['title'])),
            'upload_date': row['upload_date']
        }
        articles_list.append(dic)
    return articles_list


def save_json(articles_lst):
    with open('data/clean_articles.json', 'w', encoding='utf-8') as f:
        json.dump(articles_lst, f, ensure_ascii=False, indent=4)


json_data = pd.read_json('data/articles.json')

final_json = apply_func(json_data)
save_json(final_json)