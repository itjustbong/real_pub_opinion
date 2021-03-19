import twitter
import pandas as pd
import os


twitter_consumer_key = ""
twitter_consumer_secret = ""  
twitter_access_token = ""
twitter_access_secret = ""

twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                          consumer_secret=twitter_consumer_secret, 
                          access_token_key=twitter_access_token, 
                          access_token_secret=twitter_access_secret)


query = ["문재인", "이재명", "이낙연", "윤석열", "홍준표"]

for name in query:
    cnt = 0
    text = []
    
    statuses = twitter_api.GetSearch(term=name, count=100, since="2021-03-01")
    for status in statuses:
        text.append(status.text.strip())
        cnt += 1
    print('%s 총 검색 수 : %d'%(name,cnt))

    df = pd.DataFrame(text)
    df.columns = ["text"]
    
    if not os.path.exists("./data"):
        os.makedirs("./data")
    df.to_csv("./data/%s_twit.csv"%name, header=True, index=False, encoding="utf-8")
    print('%s_twit.csv SAVED'%name)