import requests
from bs4 import BeautifulSoup

link = 'https://nanjing.anjuke.com/sale/'

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}

r = requests.get(link, headers=headers)

soup = BeautifulSoup(r.text, 'lxml')

house_list = soup.find_all('div', class_="property-content")

for house in house_list:
    title = house.find('div', "property-content-title").h3.text.strip()
    price = house.find('div', "property-price").p.text.strip()
    price_average = house.find('p', "property-price-average").text.strip()
    if len(house.find_all('p', "property-content-info-text")) == 3:
        room = house.find_all('p', "property-content-info-text")[0].text.strip()
        area = house.find_all('p', "property-content-info-text")[1].text.strip()
        towards = house.find_all('p', "property-content-info-text")[2].text.strip()
        # floor = house.find_all('p', "property-content-info-text")[3].text.strip()
        # year = house.find_all('p', "property-content-info-text")[4].text.strip()
    else:
        room = house.find_all('p', "property-content-info-text")[0].text.strip()
        area = house.find_all('p', "property-content-info-text")[1].text.strip()
        towards = house.find_all('p', "property-content-info-text")[2].text.strip()
        floor = house.find_all('p', "property-content-info-text")[3].text.strip()
        year = house.find_all('p', "property-content-info-text")[4].text.strip()
    location = house.find('p', "property-content-info-comm-name").text.strip()
    S_location = house.find('p', "property-content-info-comm-address").text.strip()

    tags = house.find_all('span', "property-content-info-tag")
    tag = []
    for j in range(0, len(tags)):
        tag.append(tags[j].text.strip())

    txt = [title, price, price_average, room, area, towards, location,
           S_location, tag]

    print(txt)
