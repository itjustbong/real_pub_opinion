import requests
import pandas as pd 
from pprint import pprint
import json
import os
import getSuggesion

with open('config.json', 'r') as f:
    config = json.load(f)

NAVER_ID = config['NAVER']['ID'] # 'secret-key-of-myapp'
NAVER_SECRET = config['NAVER']['Secret'] # 'web-hooking-url-from-ci-service'


encode_type = 'json'
data_num = 1000
keyword = ['문재인', '이재명', '윤석열', '이낙연', '홍준표']
# keyword = ['삼성', '엘지', 'LG', '테슬라', '애플']

headers = {
    'X-Naver-Client-Id' : NAVER_ID,
    'X-Naver-Client-Secret' : NAVER_SECRET
}

for key in keyword:
    # print(key)
    url = 'https://openapi.naver.com/v1/search/news.json?query={}&display=100&sort=sim'.format(key)
    print(url)

    res = requests.get( url, headers = headers)

    if res.status_code == 200:
        datas = res.json()

        print('총 검색 수 :', datas['total'])
        print(type(datas), type(datas['items']))

        df = pd.DataFrame(datas['items'])

        if not os.path.exists("./data"):
            os.makedirs("./data")
        df.to_csv('./data/naver_{}_검색결과.csv'.format(key), encoding='utf-8', index=False)
    else:
        print(res)