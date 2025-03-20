
# ⦁	Write a Python program to construct the following pattern, using a nested loop number.
# Expected Output:

for i in range(1, 10, 2):  
    spaces = (9 - i) // 2  
    for j in range(spaces):
        print(" ", end="")  
    for j in range(i):
        print("*", end="")  
    print() 

for i in range(9, 0, -2):  
    spaces = (9 - i) // 2 
    for j in range(spaces):
        print(" ", end="")  
    for j in range(i):
        print("*", end="")  
    print()  
