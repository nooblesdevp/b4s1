import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = 'https://www.thewhiskyexchange.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
productLists = []
for x in range(1, 6):
    r = requests.get(
        'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg=2#productlist-filter')
    soup = BeautifulSoup(r.content, 'lxml')

    productList = soup.find_all('div', class_='item')

    for item in productList:
        for link in item.find_all('a', href=True):
            productLists.append(baseurl + link['href'])


testlink = 'https://www.thewhiskyexchange.com/p/33964/suntory-kakubin-yellow-label'
whiskylist = []
for link in productLists:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    name = soup.find('h1', class_='product-main__name').text.strip()
    img = soup.find('img')
    price = soup.find('p', class_="product-action__price").text.strip()
    try:
        rating = soup.find(
            'span', class_="review-overview__rating").text.strip()
    except:
        rating = 'No rating',

    whisky = {
        'name': name,
        'rating': rating,
        # 'reviews': reviews,
        'price': price,
        'img':  img
    }

    whiskylist.append(whisky)
    print('Saving',  whisky['name'])

df = pd.DataFrame(whiskylist)
print(df.head(1))
