import requests
from model import encode
from vectors import upsert, update_indexing_status
from bs4 import BeautifulSoup


def index_webpage(url, indexed_urls):
  try:
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    upsert(text, url)

    base_url = url.split('/')[2]
    links = [link.get('href') for link in soup.find_all('a')]
    links = [link for link in links if link and base_url in link]
    links = [link for link in links if link not in indexed_urls]
    links = list(set(links))
    return links
  except Exception as e:
    print(e)
    return []


def index(url):
  indexed_urls=[]
  urls = [url]

  update_indexing_status(url, 'IN_PROGRESS')

  while urls and len(indexed_urls) < 10:
    url = urls.pop()
    indexed_urls.append(url)
    urls += index_webpage(url, indexed_urls)
    urls = list(set(urls))
  
  update_indexing_status(url, 'COMPLETED')
