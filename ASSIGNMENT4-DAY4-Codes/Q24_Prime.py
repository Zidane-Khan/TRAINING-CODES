# Implement a generator function that yields all prime numbers up to a 
# given limit. 


def func_prime(N):
    for i in range(2,N+1):
        for j in range(2,i):
            if i %j ==0:
                break
        else:
            yield i

        


for i in func_prime(10):
    print(i)