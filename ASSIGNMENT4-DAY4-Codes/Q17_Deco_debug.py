# Write a decorator @debug that prints the name of the decorated 
# function before it is called. 

def debug(func):
    def wrapper(*args):
        print(f"Calling function: {func.__name__}")
        return func(*args)
    return wrapper

@debug
def greet(name):
    print(f"Hello, {name}")

greet("Zidane")