import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
    'Host': 'www.santostang.com'
}
r = requests.get('http://www.santostang.com/', headers=headers)
print(r.status_code)
