import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [23, 45, 56, 78],
    'Group': ['X', 'Y', 'X', 'Y'],
    'Scores': [10, 20, 30, 40]
}

df = pd.DataFrame(data)

# 1. Pie Chart
def plot_pie_chart():
    plt.figure(figsize=(6,6))
    plt.pie(df['Value'], labels=df['Category'], autopct='%1.1f%%', startangle=90)
    plt.title("Pie Chart")
    plt.show()

# 2. Line Plot
def plot_line_plot():
    plt.figure(figsize=(8,6))
    plt.plot(df['Category'], df['Value'], marker='o')
    plt.title("Line Plot")
    plt.xlabel("Category")
    plt.ylabel("Value")
    plt.show()

# 3. Bar Plot
def plot_bar_plot():
    plt.figure(figsize=(8,6))
    sns.barplot(x='Category', y='Value', data=df)
    plt.title("Bar Plot")
    plt.show()

# 4. Scatter Plot
def plot_scatter_plot():
    plt.figure(figsize=(8,6))
    plt.scatter(df['Value'], df['Scores'], color='blue')
    plt.title("Scatter Plot")
    plt.xlabel("Value")
    plt.ylabel("Scores")
    plt.show()



# Example Usage
plot_pie_chart()
plot_line_plot()
plot_bar_plot()
plot_scatter_plot()



# def debug(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling function: {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper

# # Example usage:
# @debug
# def greet(name):
#     return f"Hello, {name}"

# print(greet("Alice"))


# import time

# def timing(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()  # Record start time
#         result = func(*args, **kwargs)  # Call the decorated function
#         end_time = time.time()  # Record end time
#         execution_time = end_time - start_time  # Calculate execution time
#         print(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
#         return result
#     return wrapper

# # Example usage:
# @timing
# def long_running_task():
#     time.sleep(2)  # Simulate a long-running task
#     return "Task completed"

# print(long_running_task())


# import time

# def retry(retries=3, delay=1):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             attempt = 0
#             while attempt < retries:
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as e:
#                     attempt += 1
#                     print(f"Attempt {attempt} failed: {e}. Retrying in {delay} seconds...")
#                     time.sleep(delay)
#             print(f"Function {func.__name__} failed after {retries} retries.")
#             raise Exception(f"Function {func.__name__} failed after {retries} retries.")
#         return wrapper
#     return decorator

# # Example usage:
# @retry(retries=3, delay=2)
# def unreliable_task():
#     if time.time() % 2 > 1.5:  # Simulate random failure
#         return "Task succeeded"
#     else:
#         raise ValueError("Task failed")

# print(unreliable_task())


# import csv
# import re

# # Function to extract rows where email contains '@gmail.com'
# def extract_gmail_rows(file_path):
#     # Open the CSV file
#     with open(file_path, mode='r') as file:
#         # Read the CSV file
#         reader = csv.reader(file)
        
#         # Skip the header (if present)
#         headers = next(reader)
        
#         # List to store rows with @gmail.com email addresses
#         gmail_rows = []
        
#         # Loop through the rows
#         for row in reader:
#             email = row[2]  # Assuming email is in the 3rd column (index 2)
            
#             # Check if email contains @gmail.com using regex
#             if re.search(r'@gmail\.com$', email):
#                 gmail_rows.append(row)
        
#         # Return the filtered rows
#         return gmail_rows

# # Example usage:
# file_path = 'data.csv'
# gmail_rows = extract_gmail_rows(file_path)

# # Print extracted rows
# for row in gmail_rows:
#     print(row)
