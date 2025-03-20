# 56. Write a Python program that uses threading to scrape multiple web 
# pages concurrently. Use requests to fetch data and BeautifulSoup to 
# parse and extract information from multiple pages.

import threading
import requests
from bs4 import BeautifulSoup

Web=[


]

def scarp_web(web):
    response=requests.get(Web)
    if response.status_code==200:
        soup=BeautifulSoup(response.text,"html.parser")
        print(f"Page from {url}: {soup.title.string}")



for t in threads:t.start()
for t in threads:t.join()