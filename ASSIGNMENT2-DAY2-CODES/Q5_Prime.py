# ⦁	Write a Python program to check if a number is prime.

NUM=int(input("Enter Number: "))
if NUM <= 1:
    print(f"{NUM} is not a prime number.")
elif NUM==1:
    print(f"{NUM} is neither prime nor composite: ")
else:
    for i in range(2, NUM):
        if NUM % i == 0:
            print(f"{NUM} is not a prime number.")
            break
    else:
        print(f"{NUM} is a prime number.")
