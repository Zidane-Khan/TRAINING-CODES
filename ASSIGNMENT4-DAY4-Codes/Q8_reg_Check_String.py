# Write a Python program that uses a regular expression to check if the 
# string hello123 contains both letters and digits. The program should 
# return True. 

import re
String="hello"

Check=re.findall(r"\w", String)

print(Check)
print(type(Check))
flag1=False
flag2=False

for i in Check:
    if i.isdigit():
        flag1=True
    elif i.isalpha():
        flag2=True

if flag1 and flag2:
        print("The list cnatins both")

else:
     print("The list do not contains bot character and string")

  
