# imports
import requests
from bs4 import BeautifulSoup

# base url of the site to scrape
baseurl = 'https://www.thewhiskyexchange.com/'

# tells the website where the request is coming from
# without this, request is likely to be blocked due to it being a python request
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'
}


r = requests.get('https://www.thewhiskyexchange.com/customerservice/site-map', headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
siteMapLinks = soup.find_all[
#allProducts = soup.find('div', class_='twesitemap')
whiskyCategory = soup.find_all('li', class_='item-title')
whiskyAge = soup.find_all('span', class_='item-subtitle')
whiskyAge2 = soup.find_all('span', class_='item-title')
]
for item in siteMapLinks:
    for link in item.find_all('a', href=True):
        siteMapLinks.append(baseurl + link['href'])
    print(siteMapLinks)


#productlinks = []
#for x in range(1,3):
#    r = requests.get(f'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={x}')
#    soup = BeautifulSoup(r.content, 'lxml')
#    productlist = soup.find_all('li', class_='product-grid__item')
#    for item in productlist:
#        for link in item.find_all('a', href=True):
#        #for price in item.find_all('p', class_= 'product-card__price'):
#            #for title in item.find_all('p', class_= 'product-card__name'):
#                 productlinks.append(baseurl + link['href'])


#testlink = 'https://www.thewhiskyexchange.com/p/29388/suntory-hibiki-harmony'

#print(productlinks)

whiskylist = []
for link in siteMapLinks:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    name = (soup.find('h1', class_='product-main__name').text.strip())
    size = (soup.find('p', class_='product-main__data').text.strip())
    price = (soup.find('p', class_='product-action__price').text.strip())
    inStock = (soup.find('p', class_='product-action__stock-flag').text.strip())

    whisky = {
        'name': name,
        'size': size,
        'price': price,
        'inStock': inStock
    }
    print(whisky)
#whiskylist.append(whisky)
#print(whiskylist)