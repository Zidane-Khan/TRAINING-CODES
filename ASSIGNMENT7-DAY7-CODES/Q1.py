
# https://openlibrary.org/works/OL45804W.json 

# Fetch the title of the book, author and description 
import requests
import json

url="https://openlibrary.org/works/OL45804W.json"

response=requests.get(url)
data=response.json()
# print(data)
book_title=data["title"]
# author=data.get('authors')
# print(book_title)
# print(author)
for i in data['authors']:
    print(i['author'])

# import requests

# url = "https://openlibrary.org/works/OL45804W.json"
# response = requests.get(url)
# data = response.json()

# # Get the book title
# book_title = data["title"]

# # Get the description of the book
# book_description = data.get("description", "No description available.")

# # Get the author's key from the authors list (assuming there's only one author)
# author_key = data['authors'][0]['author']['key']

# # Fetch the author's details using the key
# author_url = f"https://openlibrary.org{author_key}.json"
# author_response = requests.get(author_url)
# author_data = author_response.json()

# # Get the author's name
# author_name = author_data.get('name', 'Unknown Author')

# # Print the book title, author, and description
# print(f"Book Title: {book_title}")
# print(f"Author: {author_name}")
# print(f"Description: {book_description}")

#--------------------------------------------------------------------------------------------->
# import requests
# import json
# url = "https://openlibrary.org/works/OL45804W.json"
 
# data = requests.get(url)
# # print(data)
# json_data = data.json()
# # print(json_data)
# title = json_data['title']
# author = json_data['authors'][0]['author']['key']
# # print(author)
 
# new_url = f'https://openlibrary.org{str(author)}'
# # print(new_url)
# author_data = requests.get(new_url)
# print(author_data)
# print(title)
# print('scucess',data.text)

# book_title=

# active_case=['Andaman and Nicobar Islands']['districtData']['South Andaman']['active']

# add={


#     'id':1,
#     "name": "khn"
# }

# data=requests.post(url, json=add)
# print('scucess',data.text)



# https://openlibrary.org/works/OL45804W.json 

# Fetch the title of the book, author and description 







# API_KEY="62fb545566cfe59428cf4d01ba520b0f"


# url = f'http://api.openweathermap.org/data/2.5/weather?q=london&appid={API_KEY}'

# response=requests.get(url)
# print(response.text)