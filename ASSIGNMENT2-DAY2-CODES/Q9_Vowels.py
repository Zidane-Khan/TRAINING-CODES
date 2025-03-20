#  Write a Python program to count the number of vowels in each string.


STRING="ZIDANE"
STRING2=list(STRING)

for i in STRING2:
    if i=="A" or i=="E" or i=="I" or i=="O" or i=="U" or i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        STRING2.remove(i)

print(''.join(STRING2))
