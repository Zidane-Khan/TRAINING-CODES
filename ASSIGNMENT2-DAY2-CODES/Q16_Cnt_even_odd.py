# Write a Python program to count the number of even and odd numbers in a series of numbers
# Sample numbers: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

LIST=[1, 2, 3, 4, 5, 6, 7, 8, 9]

count=0
count1=0
for i in LIST:
    if i%2==0:
        count=count+1
    else:
        count1=count1+1

print(f"COUNT OF EVEN NOS {count}, COUNT OF ODD NOS {count1}")