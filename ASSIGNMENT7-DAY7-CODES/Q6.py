# https://isro.vercel.app/api/spacecrafts
# Print all the values with ids as multiples of 5


import requests
import json


url='https://isro.vercel.app/api/spacecrafts'

response=requests.get(url)
print(response)

data=response.json()

data1 = data['spacecrafts']

for i in data1:
    if int(i['id']) % 5==0:
         print(i['name'])
