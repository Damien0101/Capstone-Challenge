import requests
import json
import datetime

lst = []

for page in range(100):
    res = requests.get(f'https://bff-service.rtbf.be/oaos/v1.5/pages/en-continu?_page={page}&_limit=100').text

    for a in json.loads(res)["data"]["articles"]:
        dict = {
            'label' : a['dossierLabel'],
            'title' : a['title'],
            'summary' : a['summary'],
            'upload_date' : str(datetime.fromisoformat(a['publishedFrom']))[:16]
        }

        lst.append(dict)

with open('articles.json', 'w') as f:
    json.dump(lst, f, ensure_ascii=False, indent=4)



