# ⦁	Write a Python program to find the first duplicate 
# element in a given array of integers. Return -1 if there are no such elements.


def find_first_duplicate(arr):

    for i in range(len(arr)):
       
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i] 
    return -1  

# Example usage
arr = [4, 5, 6, 7, 8, 4, 9]
print(find_first_duplicate(arr))  
