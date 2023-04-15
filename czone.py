from subprocess import CompletedProcess
import requests
from bs4 import BeautifulSoup
import json
import time
import array as arr

baseurl = 'https://www.czone.com.pk/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

productLinks = [] 
price = []
product_urls = []
img_urls = []


for x in range(1,12):
    r = requests.get(f'https://www.czone.com.pk/laptops-pakistan-ppt.74.aspx?page={x}')

    soup = BeautifulSoup(r.content, 'lxml')

    productList = soup.find_all('div', class_='product')


    for item in productList:
        for link in item.find_all('a', href=True):

            productLinks.append(baseurl + link['href'])
            product_urls.append(productLinks)
            # print(product_urls)
            price.append(soup.find_all(id="person_two"))
            

        for link in item.find_all('img', src=True):
            img_url = (baseurl + link['src'])
            img_urls.append(img_url)  





#testLink = 'https://www.czone.com.pk/laptops-hp-laptops-hp-15s-du1520tu-laptop-intel-celeron-n4020-4gb-ddr4-1tb-hdd-15-6-hd-display-windows-10-official-warranty-pakistan-p.12719.aspx'




names = []
prices = []
ratings = []
descriptions = []



for link in productLinks:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    name = soup.find('h1',class_='product-title').text.strip()
    print(name)

    price = soup.find('span',class_='price-sales').text.strip()

    #Rating return 0 as the rating in the website is zero stars
    rating = soup.find('div', class_='star_rating').text.strip()

    description = soup.find('div', class_="details-description").text.strip()



    names.append(name)
    prices.append(price)
    ratings.append(rating)
    descriptions.append(description)

    


    

    #print(laptop)
    #json_data = json.dumps(laptop)



laptop = {}
laptop["name"] = names
laptop["price"] = prices
laptop["rating"] = ratings
laptop["product_url"] = product_urls
laptop["img_url"] = img_urls
laptop["description"] = descriptions

with open(r"E:\Web Scrapping\laptop.json", 'a') as f:
    json.dump(laptop, f)

print("completed")










