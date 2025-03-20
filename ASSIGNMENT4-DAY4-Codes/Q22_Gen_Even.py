# 22. Write a generator function that yields all even numbers in a given range. 

def even_numbers(S,N):

    for i in range(S,N+1):
        if i%2==0:
            yield i

for i in even_numbers(1,20):
    print(i)