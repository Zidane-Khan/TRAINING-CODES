# http://openlibrary.org/people/george08/lists.json
# Fetch the list of entries with seed count less than 30

# import requests
# import json

# url='http://openlibrary.org/people/george08/lists.json'

# response=requests.get(url)
# print(response.text)

import requests


url = 'http://openlibrary.org/people/george08/lists.json'
response = requests.get(url)

# Convert the response to a JSON object
data = response.json()

# Access the "entries" list where the data is located
data_entries = data['entries']

# Loop through each entry and check the seed_count
for entry in data_entries:
    if entry['seed_count'] < 30:  # Compare the seed_count value properly
        print(f"List: {entry['name']}, Seed count: {entry['seed_count']}")
