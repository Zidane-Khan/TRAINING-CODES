# ⦁	Write a function that takes a dictionary as a keyword argument and prints each key-value pair.

def print_dict(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage
print_dict(name="Zidane", age=22)
