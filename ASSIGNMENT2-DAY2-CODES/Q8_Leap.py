# Write a Python program to check if a given year is a leap year.


YEAR = 2024  

if (YEAR % 4 == 0 and YEAR % 100 != 0) or (YEAR % 400 == 0):
    print(f"{YEAR} is a leap year.")
else:
    print(f"{YEAR} is not a leap year.")
