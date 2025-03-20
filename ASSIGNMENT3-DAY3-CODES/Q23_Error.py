# # ⦁	Write a Python program that attempts to read from a file input.txt. If an error occurs (e.g., file not found or permission denied), the program should catch the exception and log the error message to a file error.log along with the time of the error. The log file should contain the error message and a timestamp of when it occurred.
# # Example log: [2025-03-01 12:00:00] FileNotFoundError: 'input.txt' not found


# # ⦁	Write a Python program that attempts to read from a file input.txt. If an error occurs (e.g., file not found or permission denied),
# \ the program should catch the exception and log the error message to a file error.log along with the time of the error. The log file should contain the error message and a timestamp of when it occurred.
# # Example log: [2025-03-01 12:00:00] FileNotFoundError: 'input.txt' not found


import logging
from datetime import datetime

logging.basicConfig(filename='error.log', level=logging.ERROR, format='%(asctime)s - %(message)s')

try:
    with open("SRFILE.txt", 'r') as newFile:
        content = newFile.read()
        print(content)

except Exception as e:
    logging.error(f"Error: {e}")




