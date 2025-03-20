# ⦁	Write a Python program to construct the following pattern, using a nested for loop.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *


# Top half of the pattern
for i in range(1, 6):
    for j in range(i):
        print('*', end=' ')
    print()

# Bottom half of the pattern
for i in range(4, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()


