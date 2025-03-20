# ⦁	Write a function find_max() that takes a 
# list of numbers as input and returns the maximum value. Use function arguments to pass the list.


def find_max(LIST1):
    MAX = 0  
    for i in range(1, len(LIST1)):  
        if LIST1[i] > LIST1[MAX]:  
            MAX = i  
    print("The maximum value is:", LIST1[MAX])  

# Input part
N = 5  
LIST1 = []

for i in range(N):
    NUM = int(input("Enter a number for the list: "))
    LIST1.append(NUM)

find_max(LIST1)

