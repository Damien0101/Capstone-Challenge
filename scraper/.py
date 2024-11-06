import pandas as pd
import unicodedata
import spacy


json_data = pd.read_json('articles.json')


for i, row in json_data.iterrows():
    print(i, type(row['upload_date']))