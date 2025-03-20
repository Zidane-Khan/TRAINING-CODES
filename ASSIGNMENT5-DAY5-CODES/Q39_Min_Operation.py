# 39. Find the minimum number of operations (insert, delete, replace) required to 
# convert one string into another. 
# 40. Example: "horse" -> "ros" → Output: 3 

input_string="horse"
output_string="ros"

input_string1=list(input_string)
output_string1=list(output_string)


input_string2=list(output_string)


for i in output_string1:
    for j in input_string1:
        if i!=j and j not in output_string1:
            input_string1.remove(j)   
            break  
print(input_string1) 
input_string2=''.join(input_string1)
print(input_string2)

# input_string = "ros"
# input_string2 = "ors"
input_string3 = input_string2.replace('o','r')
input_string3 = input_string2.replace('r','o')
print(input_string3)

# for i in input_string:
#     for j in input_string2:
#         if i != j and j not in input_string3:
#             input_string2 = input_string2.replace(j, i)  # Replace j with i
#             input_string3.append(j)  # Mark j as processed
#             break  # Exit inner loop after replacement

# print("Final input_string2:", input_string2)

# input_string = "ros"
# input_string2 = "ors"
# input_string3 = set()  # To track processed characters in input_string2

# # Convert input_string2 to a list of characters for easier modification
# input_list = list(input_string2)

# # Iterate over each character in input_string
# for i in input_string:
#     for index, j in enumerate(input_list):
#         # If the character in input_string2 is different from the current character in input_string
#         # and hasn't been processed yet
#         if i != j and j not in input_string3:
#             input_list[index] = i  # Replace j with i at the current index
#             input_string3.add(j)  # Mark j as processed
#             break  # Exit inner loop after replacement

# # Join the modified list back into a string
# input_string2 = ''.join(input_list)

# print("Final input_string2:", input_string2)
