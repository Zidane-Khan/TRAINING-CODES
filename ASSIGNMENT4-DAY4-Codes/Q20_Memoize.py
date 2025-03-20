#  Write a decorator @memoize that caches the return value of a function and returns the cached value for the same input arguments.


valueStore = {}


def memoize(func):

    def wrapper(num):
        if num not in valueStore:
            valueStore[num] = func(num)
        return valueStore[num]
    return wrapper

@memoize
def factorial(number):
    if(number == 1 or number == 0):
        return 1
 
    return number * factorial(number - 1)

print(factorial(5))
print(factorial(5))