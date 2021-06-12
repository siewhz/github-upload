import requests
import pandas as pd
import os

def get_overview(sym):
    with open('data/apikey.txt') as f:
        apikey=f.read()
    link=f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={sym}&apikey={apikey}'
    # print(link)
    data=requests.get(link)
    data=data.json()
    data_df=pd.DataFrame.from_dict(data,orient='index').T
    return data_df

def get_ps_ratio(sym):
    data=pd.read_csv(f'data/overview_{sym}.csv')
    print(data.T)

with open('data/apikey.txt') as f:
    apikey=f.read()
sym='APTV'
print(f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={sym}&apikey={apikey}')
# data=get_overview(sym)
# data.to_csv(f'data/overview_{sym}.csv',index=False)
get_ps_ratio(sym)