# Write a Python program that validates if a phone number entered by the 
# user is in the format (xxx) xxx-xxxx, where x is a digit. Use regular 
# expressions to perform the validation. 


import re

def validate_phone_number():
    while True:
        USER = input("Please enter the phone number: ")


        if re.fullmatch(r"\(\d{3}\) \d{3}-\d{4}", USER):
            print("Correct")
            break
        else:
            print("Invalid format. Please enter the phone number in the format (xxx) xxx-xxxx.")


validate_phone_number()

