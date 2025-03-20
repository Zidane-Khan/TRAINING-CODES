# Write a Python program that parses a log file logs.txt using regular 
# expressions to find all error messages (lines containing the word 
# ERROR) and count how many there are. 



import re
LOG="ERROR ZIDANE KHAN ERROR"


CONTENT=re.findall(r"ERROR",LOG)


count=0
for i in CONTENT:
    count=count+1

print(count)
print(CONTENT)
