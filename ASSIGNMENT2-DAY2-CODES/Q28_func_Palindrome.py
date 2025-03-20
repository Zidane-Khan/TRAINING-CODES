


# ⦁	Write a function that takes a string as input and checks whether it 
# is a palindrome. A palindrome is a word that reads the same backward as forward.

def function_palindrome(STRING):
    STRING2=STRING[::-1]
    if (STRING2==STRING):
        print("THE Given String is plindrome")

    else:
        print("THE Given String is not plindrome")

function_palindrome(STRING=input("Enter String to check"))