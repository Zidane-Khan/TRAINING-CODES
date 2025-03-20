# Write a Python program to check if a given string is a palindrome.


STRING = input("Enter a string to check if it is a palindrome: ")

cleaned_string=STRING[::-1]

# Check if the string is equal to its reverse
if cleaned_string == STRING:
    print(f"'{STRING}' is a palindrome.")
else:
    print(f"'{STRING}' is not a palindrome.")
