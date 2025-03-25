


# Fetch data from https://jsonplaceholder.typicode.com/users. 
# Filter users by those with an odd user ID and sort them by their name alphabetically.

import requests
url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)

data = response.json()

List_Sort=[]

for id in data:
    if id['id']%2!=0:
        List_Sort.append(id['name'])

print(sorted(List_Sort))



# Fetch data from multiple API endpoints (https://jsonplaceholder.typicode.com/users, https://jsonplaceholder.typicode.com/posts, 
# and https://jsonplaceholder.typicode.com/comments).
# For each user, calculate the total number of comments on their posts and output the result.
