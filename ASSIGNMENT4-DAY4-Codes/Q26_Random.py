# . Create a generator function that generates a random number on each 
# iteration.   

import random

def get_random(START, END):
    for i in range(START, END):
        yield random.randint(START, END)  


for i in get_random(1, 10):
    print(i)
