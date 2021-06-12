import os
import requests
import pandas as pd

def get_value(sym,r):
    with open('data/apikey.txt') as f:
        apikey=f.read()
    symbol=sym
    data=requests.get(f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={apikey}')
    data=data.json()
    PE=data['PERatio']
    eps=data['EPS']
    value=float(PE)*(1+r)*float(eps)
    print(value)

# intrin_value=pe*(1+r)*eps

get_value('APTV',0.1)