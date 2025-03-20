#  Write a Python program that finds all words in the string "This is a test 
# sentence." using regular expressions and stores them in a list

import re

STRING="This is a test sentence."

FIND=re.findall(r'\w', STRING)

print(FIND)