from concurrent.futures import ThreadPoolExecutor
import requests
import datetime
import json


def scraper(urls):
    lst = []
    
    for page in range(100):
        res = requests.get(urls).text

        for a in json.loads(res)["data"]["articles"]:
            articles = {
                'label' : a['dossierLabel'].lower(),
                'title' : a['title'].lower(),
                'summary' : a['summary'].lower(),
                'upload_date' : str(datetime.datetime.fromisoformat(a['publishedFrom']))[:16]
            }

            lst.append(articles)
    return lst

def save_file(data):
    with open('data/articles.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

urls = [str(f'https://bff-service.rtbf.be/oaos/v1.5/pages/en-continu?_page={page}&_limit=100') for page in range(10)]

with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(scraper, urls))[0]


save_file(results)



