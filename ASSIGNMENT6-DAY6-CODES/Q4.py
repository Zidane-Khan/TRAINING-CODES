# #  6 

# # 1 2 2 6 5 1 

# # Sample Output 1 

# #  2 6 

# # 3 6 

# # 2 6 

# # 2 5 

# # 2 4 

# # # 1 4 

# # arr = [1, 2, 2, 6, 5, 1]
# # OFF='OF'
# # ON='ON'
# # for i in range(len(arr)):

# #     arr[i]=ON
# #     # print(arr[i])

# # for i in range(len(arr)):

# #     if 


# for i in range(len(arr)):
#     if i + 1 < len(arr): 
#         arr[i]=OFF
#         if arr[i+1] == ON:
#             for j in range(len(arr),1,-1):
#                 if j + 1 < len(arr): 
#                     if arr[j]==ON:
#                         print(i+2 ,j+1)
#                     break

# # arr = [1, 2, 3, 4, 5]  # Example array

# # for i in range(len(arr)):
# #     print(f"Index {i+1}: {arr[i]}")  # i+1 gives the 1-based index



# arr = [1, 2, 3, 6, 5, 1]
# OFF = 'OF'
# ON = 'ON'

# N = 6
# bulbs = [ON] * N  # All bulbs start as ON

# # The operations (which bulbs to toggle)
# arr = [1, 2, 2, 6, 5, 1]

# # Process each operation in the arr array
# for i in range(len(arr)):

#     bulb_index = arr[i] - 1  # arr[i] = 1 means bulb 1, which corresponds to index 0
    
#     if bulbs[bulb_index] == ON:
#         bulbs[bulb_index] = OFF  # Turn it OFF if it was ON
#     else:
#         bulbs[bulb_index] = ON   # Turn it ON if it was OFF

#     # Print the current state of the bulbs after each toggle
#     print(bulbs)





# N = 6
# arr = [1, 2, 2, 6, 5, 1]
# OFF = 'OF'
# ON = 'ON'

# bulbs = [ON] * N  # Initially all bulbs are ON
# for i in range(len(arr)):
#     # Flip the bulb at position arr[i] - 1 (convert to 0-based index)
#     bulb_index = arr[i] - 1

#     if bulbs[bulb_index] == ON:
#         bulbs[bulb_index] = OFF  # Turn it OFF if it was ON

#         first_on_left = -1
#         for j in range(N):
#             if bulbs[j]:  # Bulb is ON
#                 first_on_left = j + 1  
#                 break
#     else:
#         bulbs[bulb_index] = ON     
#         first_on_right = -1
#         for j in range(N-1, -1, -1):
#             if bulbs[j]:  # Bulb is ON
#                 first_on_right = j + 1  
    
#     # Output the result for this operation
#     print(first_on_left, first_on_right)



# Input
# N = 6
# arr = [1, 2, 2, 6, 5, 1]

# # Initialize all bulbs as ON
# bulbs = [True] * N  # True represents ON, False represents OFF

# # Process each toggle operation
# for i in range(N):
#     # Toggle the bulb at position arr[i] - 1 (convert to 0-based index)
#     bulb_index = arr[i] - 1
    
#     # Toggle the bulb state (ON -> OFF or OFF -> ON)
#     bulbs[bulb_index] = not bulbs[bulb_index]
    
#     # Find the first ON bulb from left to right
#     first_on_left = -1
#     for j in range(N):
#         if bulbs[j]:  # Bulb is ON
#             first_on_left = j + 1  # 1-based index
#             break
    
#     # Find the first ON bulb from right to left
#     first_on_right = -1
#     for j in range(N-1, -1, -1):
#         if bulbs[j]:  # Bulb is ON
#             first_on_right = j + 1  # 1-based index
#             break
    
#     # Output the results for this operation
#     print(first_on_left, first_on_right)

# Initialize input
N = 6  # Number of bulbs
arr = [1, 2, 2, 6, 5, 1]  # Array indicating which bulb to toggle

# Initialize all bulbs as ON
ON = "ON"
OFF = "OFF"
bulbs = [ON] * N  # All bulbs start as ON

# Process each toggle operation
for i in range(N):
    # Convert bulb number from 1-based to 0-based index
    bulb_index = arr[i] - 1
    
    # Toggle the bulb (if it's ON, make it OFF; if it's OFF, make it ON)
    if bulbs[bulb_index] == ON:  # If the bulb is ON
        bulbs[bulb_index] = OFF  # Turn it OFF
    else:  # If the bulb is OFF
        bulbs[bulb_index] = ON  # Turn it ON

    # Query 1: Find the first ON bulb from left to right
    first_on_left = -1
    for j in range(N):
        if bulbs[j] == ON:  # Bulb is ON
            first_on_left = j + 1  # 1-based index
            break
    
    # Query 2: Find the first ON bulb from right to left
    first_on_right = -1
    for j in range(N-1, -1, -1):
        if bulbs[j] == ON:  # Bulb is ON
            first_on_right = j + 1  # 1-based index
            break
    
    # Output the result after the current toggle
    print(first_on_left, first_on_right)
