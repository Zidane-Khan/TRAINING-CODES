# Program Write a Python program to edit an element in a tuple.

TUPLE=("A","B","D")
print("Your tuple before editing an element ", TUPLE)
STRING=list(TUPLE)
print(STRING)
STRING.remove("D")
STRING.append("Z")
STRING2=tuple(STRING)
print("Your tuple after editing an element ", STRING2)
