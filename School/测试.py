import requests
from bs4 import BeautifulSoup
import pymysql

conn = pymysql.connect(host='localhost', user='root', passwd='root', db='Spider')
cur = conn.cursor()


def storage(title1, time1, txt1):
    cur.execute("insert into spider (title, time, article) values (%s, %s, %s)", (title1, time1, txt1))
    cur.close()
    conn.commit()
    conn.close()


link = 'https://www.njcit.cn/2023/0506/c3989a138617/page.psp'

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}

r = requests.get(link, headers=headers)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, "lxml")

article = soup.find('div', class_="article")

title = article.h1.text.strip()
time = article.p.span.text.strip()[3:]
txt = article.find('article', class_="read").text.strip()
print(title, time)
print(txt)
storage(title, time, txt)