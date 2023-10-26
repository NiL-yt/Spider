import requests
import json

link = 'https://api-zero.livere.com/v1/comments/list?callback=jQuery112407430501671387877_1682583305309&limit=10&repSeq=4345238&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&code=&_=1682583305311'
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
