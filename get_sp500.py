import requests
import json

link=f'https://pkgstore.datahub.io/core/s-and-p-500-companies/constituents_json/data/53978ce4c8df22cd5fde7a80b2041f25/constituents_json.json'
# print(link)
data=requests.get(link)
data=data.json()
for item in data:
    print(item['Symbol'])