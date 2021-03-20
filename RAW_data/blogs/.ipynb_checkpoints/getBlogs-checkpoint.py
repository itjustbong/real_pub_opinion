import os
import sys
import urllib.request
import datetime
import time
import json
import getSuggestion
import pandas as pd

client_id = 'CNriD43CN2mK9HvphC9_'
client_secret = 'oK6Wxys2YC'

def getRequestUrl(url):    
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)
    
    try: 
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print ("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
        
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None
    
def getNaverBlogSearch(query, start, display):
    base = "https://openapi.naver.com/v1/search/blog.json"
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(query), start, display)
    
    url = base + parameters    
    responseDecode = getRequestUrl(url)
    
    if (responseDecode == None):
        return None
    else:
        return json.loads(responseDecode)
    

def main():
    query = ["문재인", "이재명", "이낙연", "윤석열", "홍준표"]
    
    ##추가 for get 연관검색어
    suggestion = []
    
    for i in query:
        data_arr = getSuggestion.getSugList(i)
        for k in data_arr:
            suggestion.append(k)
            print(k)
            
    query.extend(suggestion)
    ##
    
    for name in query:
        cnt = 0
        text = []
        created_at = []

        jsonResponse = getNaverBlogSearch(name, 1, 100)
        for blog in jsonResponse['items']:
            text.append(blog['description'])
            created_at.append(blog['postdate'])
            cnt += 1
        print('%s 총 검색 수 : %d'%(name,cnt))
    
        if len(text)==0 :
            continue

        df1 = pd.DataFrame(text)
        df2 = pd.DataFrame(created_at)
        df = pd.concat([df1,df2], axis=1)
        df.columns = ["text","created_at"]

        if not os.path.exists("./data"):
            os.makedirs("./data")
        df.to_csv("./data/%s_blog_naver.csv"%name, header=True, index=False, encoding="utf-8")
        print('%s_blog_naver.csv SAVED'%name)
    
    
if __name__ == '__main__':
    main()