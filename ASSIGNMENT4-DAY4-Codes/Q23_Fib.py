# 23. Create a generator function that generates Fibonacci numbers. 


def FIBO(RANGE):
    A=0
    B=1

    for i in range(RANGE):
        yield A
        A, B = B, A + B
        # yield A


for i in FIBO(10):
    print(i,end=" ")