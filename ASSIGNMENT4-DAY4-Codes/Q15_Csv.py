# 15. Write a Python program that reads a CSV file data.csv and uses regular 
# expressions to extract all rows where the email address contains 
# @gmail.com. 



import csv
import re

# Path to your CSV file
My_File = "C:\\Users\\Zidane Khan\\Downloads\\sample-csv-files-sample4.csv"

with open(My_File, 'r') as file:
    reader = csv.reader(file)

    headers = next(reader)

    for row in reader:
        email = row[1]  
        if re.search(r"@gmail.com", email):
            print(row)


