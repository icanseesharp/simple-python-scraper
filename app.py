'''
Following script is written purely for learning & self help purpose.
Author : Sagar Yerva
'''

import requests
from bs4 import BeautifulSoup
import openpyxl 

base_url = "https://housing.com/in/buy/searches/"
area_ids = "P1pu1fhmtcb6ffmti" #this id is for kharadi area in pune
full_url = base_url + area_ids

# Get Page response in HTML and parse using BeautifulSoup
page = requests.get(full_url)
soup = BeautifulSoup(page.content, "html.parser")
articles = soup.findAll('article')

# each div with an element <article> holds a property listing
for article in articles:
    name= article.find('h2').text
    price = article.find('div', class_="css-18rodr0").text
    price_per_sq_ft = article.find_all('div', class_="css-4z3njv")
    print(f'{name} : {price}')
    for feature in price_per_sq_ft:
        print(feature.text)

print('done!')