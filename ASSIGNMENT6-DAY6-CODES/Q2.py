# n=int(input("how many no yu want"))
# for i in range(8):
#     NUM=int(input("enter nos"))
# #     NUM1=NUM.split(' ')
arr = [1, 3, 5, 4, 1, 5, 3, 6]
# arr=[1 ,3 ,2, 4, 4, 5, 3, 6]
# round = 1  # To keep track of the number of rounds

# # Loop through array, except the last element
# for i in range(len(arr) - 1):
#     if arr[i] < arr[i + 1]:
#         print(arr[i],arr[i+1])
#         round = round + 1
#     else:
#         round = round - 1

# print(f"Rounds: {round}")

rounds = 1  # Start with the first round
for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:  # If the height is not strictly greater than the previous one
            rounds += 1  # A new round is needed
    
print(rounds)



