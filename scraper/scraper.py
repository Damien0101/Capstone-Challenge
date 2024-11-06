import requests
import datetime
import json


def scraper(lst = []):
    for page in range(100):
        res = requests.get(f'https://bff-service.rtbf.be/oaos/v1.5/pages/en-continu?_page={page}&_limit=100').text

        for a in json.loads(res)["data"]["articles"]:
            dict = {
                'label' : a['dossierLabel'].lower(),
                'title' : a['title'].lower(),
                'summary' : a['summary'].lower(),
                'upload_date' : str(datetime.datetime.fromisoformat(a['publishedFrom']))[:16]
            }

            lst.append(dict)
    return lst

def save_file(data):
    with open('articles.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

data = scraper()
save_file(data)



