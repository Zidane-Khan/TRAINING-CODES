# Implement a caching mechanism to avoid making repeated API requests. If data has already been fetched for a specific user.
# API: https://jsonplaceholder.typicode.com/users


import requests
url = 'https://jsonplaceholder.typicode.com/users'
cache={}

def get_user():
    return cache.setdefault('users',requests.get('https://jsonplaceholder.typicode.com/users.json()'))

print(get_user())
print(get_user())











