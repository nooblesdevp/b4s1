import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

res = requests.get(
    'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg=2#productlist-filter')

soup = BeautifulSoup(res.content, 'lxml')

product = soup.find('img', class_="product-main__image")['src']

print(product)
