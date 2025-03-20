# 52. Write a Python program where two threads increment a shared variable  counter. Use a threading
# .Event to control the start of both threads and  ensure they increment the counter simultaneously.

import threading

counter = 0

# Lock to protect the shared variable
counter_lock = threading.Lock()

# Event to control the start of threads
start_event = threading.Event()

# Function to increment the counter
def increment_counter():
    global counter

    start_event.wait()
    for _ in range(100000):
        # Lock the shared counter to ensure thread safety
        with counter_lock:
            counter += 1

# Create two threads
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

# Start both threads
thread1.start()
thread2.start()

# Set the event to allow threads to start incrementing the counter simultaneously
start_event.set()

# Wait for both threads to finish
thread1.join()
thread2.join()

print(f"Final counter value: {counter}")
