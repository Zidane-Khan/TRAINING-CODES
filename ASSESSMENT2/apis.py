# You are tasked with building a Python program that interacts with a public API. 
# The API provides a list of users, each with a name and a unique ID. 
# Your goal is to write a Python script that fetches this list of users from the API and performs the following actions:
# Fetch the list of users: The API endpoint is https://jsonplaceholder.typicode.com/users.
# Filter the list: Find all users whose name contains the "i".
# Sort the list: After filtering, sort the users alphabetically by their name.
# Output the result: Print the names and IDs of the filtered and sorted users.
# You are given the URL https://jsonplaceholder.typicode.com/users for fetching the data.
# Your Python program should make a GET request to this API, filter the results based on the name, sort them, and print the sorted list.

import requests
url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)

# Convert the response to a JSON object
data = response.json()

# Filter the list: Find all users whose name contains the "i".
stringi='i'
List_i={}
for i in data:
   if stringi in i['name']:
    #   List_i.append(i['id'])
    #   List_i.append(i['name'])
      List_i.update({i['id']:i['name']})
print(List_i)
# Sort the list: After filtering, sort the users alphabetically by their name.

Sort_List=dict(sorted(List_i.items(), key=lambda item:(item[0],item[1])))

# # for id in data:
# #    if id in Sort_List:
# #       print(id['id'])
      
print(Sort_List)









