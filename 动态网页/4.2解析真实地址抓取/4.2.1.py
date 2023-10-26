import requests
import json


def single_page_comment(link):
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
        'Host': 'api-zero.livere.com'
    }
    r = requests.get(link, headers=headers)
    json_string = r.text
    json_string = json_string[json_string.find('{'):-2]
    json_data = json.loads(json_string)
    comment_list = json_data['results']['parents']
    for eachone in comment_list:
        message = eachone['content']
        print(message)


for page in range(1, 4):
    link1 = 'https://api-zero.livere.com/v1/comments/list?callback=jQuery112404360369487877185_1682584132724&limit=10&offset='
    link2 = '&repSeq=4345238&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&code=&_=1682584132731'
    page_str = str(page)
    link = link1 + page_str + link2
    print(link)
    single_page_comment(link)
