# Implement a caching mechanism to avoid making repeated API requests. If data has already been fetched for a specific user.
# API: https://jsonplaceholder.typicode.com/users


# import requests

# dict = {}
url = 'https://jsonplaceholder.typicode.com/users'


import requests
from requests_cache import CachedSession

session = CachedSession('api_cache', expire_after=300)

def fetch_data(url):
    response = session.get(url)

data = fetch_data(url)
print(data)

