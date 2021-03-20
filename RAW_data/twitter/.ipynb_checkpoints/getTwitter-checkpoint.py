import twitter
import pandas as pd
import os
import getSuggestion

twitter_consumer_key = ""
twitter_consumer_secret = ""  
twitter_access_token = ""
twitter_access_secret = ""

twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                          consumer_secret=twitter_consumer_secret, 
                          access_token_key=twitter_access_token, 
                          access_token_secret=twitter_access_secret)


query = ["문재인", "이재명", "이낙연", "윤석열", "홍준표"]
##추가 for get 연관검색어
suggestion = []

for i in query:
    data_arr = getSuggestion.getSugList(i)
    for k in data_arr:
        suggestion.append(k)
        print(k)
##

query.extend(suggestion)

for name in query:
    cnt = 0
    text = []
    created_at = []
    comp = []
    isSame = False
    
    statuses = twitter_api.GetSearch(term=name, count=100)
    for status in statuses:
        for c in comp:
            if c == status.text[:20]:
                isSame = True
                break
        if isSame:
            continue
        text.append(status.text.strip())
        created_at.append(status.created_at)
        comp.append(status.text[:20])
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
    df.to_csv("./data/%s_twit.csv"%name, header=True, index=False, encoding="utf-8")
    print('%s_twit.csv SAVED'%name)