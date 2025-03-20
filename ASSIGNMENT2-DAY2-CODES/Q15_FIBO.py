

# ⦁	Write a Python program to print the Fibonacci sequence.
# Note: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

NUM = int(input("Enter the number of terms in Fibonacci sequence: "))
    
A=0
B=1
for i in range(NUM):
    print(A, end=' ')
    A, B = B, A + B
    # A=B
    # B=A+B

