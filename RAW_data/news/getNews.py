import requests
import pandas as pd 
from pprint import pprint


encode_type = 'json'
data_num = 1000
keyword = ['문재인', '이재명', '윤석열', '이낙연', '홍준표']
# keyword = ['삼성', '엘지', 'LG', '테슬라', '애플']

headers = {
    'X-Naver-Client-Id' : 'UlYgMB3RI252lyb5TT9h',
    'X-Naver-Client-Secret' : 'N30oS9vD5m'
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
        df.to_csv('naver_{}_검색결과.csv'.format(key), encoding='utf-8', index=False)
    else:
        print(res)