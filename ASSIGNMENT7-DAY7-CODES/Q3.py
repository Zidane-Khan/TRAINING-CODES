# www.themealdb.com/api/json/v1/1/categories.php
# Fetch the list of food products with idCategory greater than 8

# import requests
# import json
# url='https://www.themealdb.com/api/json/v1/1/categories.php'

# response=requests.get(url)
# data=response.json()
# print(response.text)


# data1=data['categories'][0]

# print(data1)


import requests
import json

url = 'https://www.themealdb.com/api/json/v1/1/categories.php'

response = requests.get(url)
data = response.json()

# Printing the whole response to inspect the structure
print(response.text)

data1 = data['categories']

n=len(data1)

# Printing the whole category data for inspection
print(data1)

# Extracting the 'idCategory' from the first category

for item in  data1:
    if int(item['idCategory']) > 8:
        print(item['strCategory'])
        print(item['strCategoryDescription'])
        # print(item['idCategory'])



# # Printing the idCategory
# print("idCategory:", id_category)



import requests
 
# url = "https://www.themealdb.com/api/json/v1/1/categories.php"
# data = requests.get(url)
# json_data = data.json()
# id = json_data["categories"]
# num = len(id)
# for i in range(7,num):
#     id = json_data["categories"][i]
#     print(id)