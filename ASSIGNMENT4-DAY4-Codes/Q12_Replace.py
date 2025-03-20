# Write a Python program that uses a regular expression to replace all 
# occurrences of the word "apple" with "orange" in the string "apple pie is 
# apple-flavored". The output should be "orange pie is orange-flavored". 



import re

STRING="apple pie is apple-flavored"
FIND=re.sub(r'apple','orange',STRING)

print(FIND)



