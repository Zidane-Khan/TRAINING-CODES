NUM = []
for i in range(2):
    OPERATION = input("Enter operations: ")
    OPR1 = OPERATION.split(" ")
    for i in OPR1:
        if i.isdigit():  # Corrected the method call by adding parentheses
            NUM.append(i)

print(NUM)

# if OPERATION.isdigit:
#     print(OPERATION)

# use parethhsisi