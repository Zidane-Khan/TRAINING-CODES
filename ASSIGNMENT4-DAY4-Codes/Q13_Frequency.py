#  Write a Python program that uses the re module to find the frequency of 
# each word in a text file text.txt. Ignore case and punctuation. 


import re

STRING="This is a test sentence sentence?!!."

FIND=re.findall(r'\w+', STRING)

print(FIND)
LIST={}


for i in FIND:
    if i in LIST:
        LIST[i]=LIST[i]+1
    else:
        LIST[i]=1

print(LIST)
    


    







