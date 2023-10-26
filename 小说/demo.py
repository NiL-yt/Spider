import requests
from bs4 import BeautifulSoup

url = 'https://pandamtl.com/another-world-milf-hunter-1/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup)
# 根据该网页的结构，以下选择器可能可以定位到小说的内容
# 请注意，具体的选择器可能需要根据实际的HTML结构进行调整
novel_content = soup.find('div', class_='epcontent entry-content')

if novel_content:
    text = novel_content.get_text()
    with open('novel.txt', 'w', encoding='utf-8') as file:
        file.write(text)
else:
    print("没有找到小说内容")

