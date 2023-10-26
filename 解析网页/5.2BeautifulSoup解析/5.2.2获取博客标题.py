import requests
from bs4 import BeautifulSoup

link = 'http://www.santostang.com/'
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}
r = requests.get(link, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")
first_title = soup.find("h1", class_="post-title").a.text.strip()
print(first_title)

for child in soup.header.descendants:
    print(child)
