import time
import requests
import pandas as pd
from bs4 import BeautifulSoup 


YOURAPIKEY = '32367######c3906cfc2#####90' #Scraperapi tools to rotation proxy

def status_code(url):
    # function to check the response status code, exemple : status HTTP 200
    payload = {'api_key': YOURAPIKEY, 'url':url}
    response = requests.get('http://api.scraperapi.com', params=payload)
    return response.status_code


def html_parser(url):
    # function to parse the html DOM as text 
    payload = {'api_key': YOURAPIKEY, 'url':url}
    response = requests.get('http://api.scraperapi.com', params=payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


status = status_code('http://www.cdiscount.com/telephonie/telephone-mobile/apple/iphone-11-pro/l-144043125.html#_his_')

main_page = html_parser('http://www.cdiscount.com/telephonie/telephone-mobile/apple/iphone-11-pro/l-144043125.html#_his_')



page_link = []

for element in main_page.findAll('div', attrs={'class':'prdtBILDetails'}):
    for elem in element.findAll('a'):
        page_link.append(elem.get('href'))

name_phone = []
price_phone = []
location_price = []
availability_phone = []


for url in page_link:

    status = status_code(url)
    time.sleep(3)
    response = html_parser(url)

    
    phone = response.find('h1', attrs={'itemprop':'name'}).text
    name_phone.append(phone)
    
    price = response.find('span', attrs={'class':'fpPrice price jsMainPrice jsProductPrice'}).text
    price_phone.append(price)

    location = response.find('div', attrs={'class':'fpRentalChoicePrice jsClassicPrice'}).text
    location_price.append(location)

    availability = response.find('p', attrs={'class':'fpProductAvailability'}).text
    availability_phone.append(availability)
    break # Delete the break to process all pages


# Data Frame creation as CSV 
df = pd.DataFrame({'Phone':name_phone})
df['Price'] = price_phone
df['Price-Location'] = location_price
df['Availability'] = availability_phone

df.to_csv("iphone_2019.csv", encoding="utf-8-sig", index=False)
