# . Write a generator function that returns the powers of a number up to a 
# specified exponent. 


import math

def get_power(N,E):
    for i in range(1,EXP+1):
        POWERS= NUM**i
        # print(POWERS)
        yield POWERS


#         NUM**i
#         print( NUM)
        

NUM=int(input("Enter given no"))
EXP=int(input("Enter Exponent"))
get_power(NUM,EXP)
for i in get_power(NUM,EXP):
    print(i)