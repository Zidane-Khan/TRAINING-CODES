# https://api.chucknorris.io/jokes/random
# Print the ‘value’ attribute for 5 instances

import requests
import json


url='https://api.chucknorris.io/jokes/random'
response=requests.get(url)

data=response.json()

print(data['value']*5)