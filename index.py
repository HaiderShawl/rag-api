import requests
from model import encode
from vectors import upsert
from bs4 import BeautifulSoup

url = 'https://help.octaneai.com/en/collections/9496268-developer-docs'

def index_webpage(url, indexed_urls):
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


def index_website(url):
  indexed_urls=[]
  urls = [url]

  while urls and len(indexed_urls) < 100:
    url = urls.pop()
    indexed_urls.append(url)
    urls += index_webpage(url, indexed_urls)
    urls = list(set(urls))


index_website(url)