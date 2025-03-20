# arr=[1 ,2, 3, 4, 3] 

# for i in range(len(arr)):
#     if arr[i]<arr[i+1]:
#         print(arr[i+1])
        

# arr = [1, 2, 3, 4, 3]
# n = len(arr)

# for i in range(n):
#     # Using modulus to avoid index out of bounds error
#     next_index = (i + 1) % n  # This ensures that the index wraps around to 0 when it reaches n-1
#     if arr[i] < arr[next_index]:
#         print(arr[next_index])
#     else:
#         print(-1)
arr = [1, 3 , 2 , 1, 8, 4,0]
n = len(arr)

for i in range(n):
    # Start searching for the next greater element in a circular manner
    next_greater_found = False
    for j in range(1, n):  
        next_index = (i + j) % n
        if arr[next_index] > arr[i]:
            print(arr[next_index])
            next_greater_found = True
            break
    
    # If no greater element found, print -1
    if not next_greater_found:
        print(-1)

