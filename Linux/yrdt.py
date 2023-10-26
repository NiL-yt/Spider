import requests
from bs4 import BeautifulSoup
import time
import pymysql


def storage(title1, time1, txt1):
    conn = pymysql.connect(host='localhost', user='root', passwd='Root1234!', db='Spider')
    cur = conn.cursor()
    cur.execute("insert into yrdt (title, time, article, section) values (%s, %s, %s, %s)",
                (title1, time1, txt1, '育人动态'))
    cur.close()
    conn.commit()
    conn.close()


i = '1'

link1 = 'https://www.njcit.cn'
link2 = '/yrdt/list' + i + '.htm'

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}

r = requests.get((link1 + link2), headers=headers)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, "lxml")

all_pages = soup.find('em', class_="all_pages").text.strip()

news = soup.find('div', class_="column-news-list clearfix")

news_list = news.find_all('a', class_="clearfix")

for page in range(1, int(all_pages) + 1):
    link_page = 'https://www.njcit.cn/yrdt/list' + str(page) + '.htm'
    print(link_page)

    re = requests.get(link_page, headers=headers)
    re.encoding = 'utf-8'
    sop = BeautifulSoup(re.text, "lxml")

    news = sop.find('div', class_="column-news-list clearfix")

    news_list = news.find_all('a', class_="clearfix")

    for href in news_list:
        url = href.get('href')
        print(link1 + url)
        res = requests.get((link1 + url), headers=headers)
        res.encoding = 'utf-8'
        sp = BeautifulSoup(res.text, "lxml")
        article = sp.find('div', class_="article")
        title = article.h1.text.strip()
        times = article.p.span.text.strip()[3:]
        txt = article.find('article', class_="read").text.strip()
        print(title, times)
        print(txt)
        storage(title, times, txt)
        time.sleep(1.5)
