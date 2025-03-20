

# ⦁	Write a recursive function that calculates the factorial of a number.
# The function should handle the base case (n == 0) and recursive case (n > 0).

def factorial(n):
  
    if n == 0:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)


print(factorial(5))  
