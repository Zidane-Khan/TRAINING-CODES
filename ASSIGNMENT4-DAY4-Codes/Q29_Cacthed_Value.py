# 29. Write a decorator that caches the results of expensive function calls and returns the 
# cached result when called with the same arguments. 

cache = {}

def cache_results(func):
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@cache_results
def expensive_function(x, y):
    print("Calculating...")
    return x * y

print(expensive_function(2, 3))
print(expensive_function(2, 3))
