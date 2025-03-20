# 9. Create a decorator @retry that retries executing a function a specified 
# number of times if an exception occurs. 


import time

# Define the retry decorator
def retry(max_retries):
    def decorator(func):
        def wrapper():
            attempts = 0
            while attempts < max_retries:
                try:
                    return func()  # Try calling the original function
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")  # Print the error
                    if attempts == max_retries:  # If we've tried the max number of times, raise the error
                        print("Max retries reached. Giving up!")
                        raise
                    time.sleep(1)  # Wait for 1 second before retrying
        return wrapper
    return decorator


@retry(max_retries=3)  # Try 3 times if the function fails
def my_function():
    print("Trying to run function...")
    x = 1 / 0  # This will cause a division by zero error

# Call the function
my_function()
