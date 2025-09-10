import pandas as pd
import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from config import PATHS

def load_url_mapping_xlsx(file):
    df = pd.read_excel(file)
    url_map = dict(zip(df['URL_ID'].astype(str), df['URL']))
    return url_map
def scrape_article(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1').get_text(strip=True) if soup.find('h1') else ''
        paragraphs = soup.find_all('p')
        article = ' '.join([p.get_text(strip=True) for p in paragraphs])
        return f"{title}\n{article}"
    except Exception as e:
        print(f"❌ Failed to scrape {url}: {e}")
        return ""
    
def retreive_url():
    url_map=load_url_mapping_xlsx(PATHS['input'])
    os.makedirs(PATHS['articles'], exist_ok=True)
    for url_id, url in tqdm(url_map.items(), total=len(url_map)):
        text = scrape_article(url)

        with open(f"{PATHS['articles']}/{url_id}.txt", 'w', encoding='utf-8') as f:
            f.write(text)

    return

