# https://coronavirus.m.pipedream.net/
# Fetch a list of all entries of the following countries with their death counts and last update timestamp : 
# Canada , China , India , Africa



import requests
import json

url = "https://coronavirus.m.pipedream.net/"

response = requests.get(url)
data = response.json()


countries_of_interest = ["Canada", "China", "India", "Africa"]


filtered_data = []

for entry in data['rawData']:
    country = entry.get('Country_Region')
    if country in countries_of_interest:
        country_data = {
            'Country': country,
            'Deaths': entry.get('Deaths', 'N/A'),
            'Last_Update': entry.get('Last_Update', 'N/A')
        }
        filtered_data.append(country_data)


print(json.dumps(filtered_data, indent=4))

