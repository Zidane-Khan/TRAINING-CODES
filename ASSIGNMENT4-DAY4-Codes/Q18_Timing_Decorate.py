# 18. Implement a decorator @timing that measures and prints the execution 
# time of a function. 


import time

# This is the decorator
def timing(func):
    def wrapper():
        start_time = time.time()  # Record the start time
        func()  # Call the function
        end_time = time.time()  # Record the end time
        print(f"Execution time: {end_time - start_time} seconds")  # Print raw execution time
    return wrapper

# This is the function we will apply the decorator to
@timing
def simple_function():
    print("Running the function...")
    time.sleep(1)  # Simulate a delay of 1 second


simple_function()
