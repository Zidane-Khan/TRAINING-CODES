# Write a Python program to find the maximum and minimum elements in a list.
LIST = [8, 2, 7, 2, 3, 5]
MAX = 0  
MIN = 0  

for i in range(1, len(LIST)):  
    if LIST[i] > LIST[MAX]:  
        MAX = i
    elif LIST[i] < LIST[MIN]:  
        MIN = i

print("Maximum value is: ", LIST[MAX])  # Maximum value
print("Minimum value is: ",LIST[MIN])  # Minimum value