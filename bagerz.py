from subprocess import CompletedProcess
import requests
from bs4 import BeautifulSoup
import json
import array as arr

baseurl = 'https://www.bagerz.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

logo_url = 'cdn.shopify.com/s/files/1/0493/4939/4585/files/logo_svg_140x.jpg?v=1649851249'
productLinks = [] 
price = []
product_urls = []
img_urls = []

# for x in range(1,7):
r = requests.get(f'https://www.bagerz.com/collections/sale?page=1')

soup = BeautifulSoup(r.content, 'lxml')

productList = soup.find_all('div', class_="col-lg-12 col-12")

for item in productList:
    for link in item.find_all('a', href=True):
        productLinks.append(baseurl + link['href'])
        product_urls.append(productLinks)
        # print(baseurl + link['href'])
        

    for link in item.find_all('img', src=True):
        img_url = link['src']
        img_url = img_url.strip("//")
        img_urls.append(img_url)
        # print(img_url)




names = []
norm_prices = []
disc_prices = []
descriptions = []



for link in productLinks:
    r = requests.get(link,headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    name = soup.find('h1', class_='product_title entry-title').text.strip()
    print(name)

    norm_price = soup.find('p', class_="price_range").find('del').text.strip()

    # print(norm_price)

    disc_price = soup.find('p', class_='price_range').find('ins').text.strip()

    # print(disc_prices)

    description = soup.find('p', class_='mg__0').text.strip()

    # print(description)

    names.append(name)
    disc_prices.append(disc_price)
    norm_prices.append(norm_price)
    descriptions.append(description)





bagerz = {}
bagerz['logo_url'] = logo_url
bagerz['name'] = names
bagerz['norm_prices'] = norm_prices
bagerz['disc_prices'] = disc_prices
bagerz['product_url'] = productLinks
bagerz['image_url'] = img_urls
bagerz['description'] = descriptions

with open(r"E:\Web Scrapping\bagerz.json", 'a') as f:
    json.dump(bagerz, f)


print("completed")



