# arr=[3 ,2 ,1]
# arr1=[1, 3, 2]
# # arr2=[]

# count=0

# for i in range(len(arr)):
#     for j in  range(len(arr1)):
#         if arr[i]==arr1[j]:
#             arr.remove(arr[i])
#             count=count+1
#         else:
#              arr=arr[1:] + [arr[0]]
#              count=count+1
#         break
# print(count)

# wghile to cehck if lost is empty or not


arr = [1,2,3]
arr1 = [3,2,1]
count = 0


# processed = []

while arr:
    # Check if the first element in arr matches the first element in arr1
    if arr[0] == arr1[0]:
        arr.pop(0) 
        arr1.pop(0)  
        count += 1   # Increment time
    else:
   
        arr = arr[1:] + [arr[0]]
        count += 1   # Increment time for rotation

print(count)

           

    
