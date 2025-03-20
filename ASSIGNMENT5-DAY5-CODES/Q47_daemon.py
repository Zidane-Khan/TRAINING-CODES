#  Write a Python program that creates a background daemon thread that 
# prints "Hello from the daemon thread" every 2 seconds. The main 
# program should run for 5 seconds and then exit. 


import threading
import time



def hello():
    while True:
        print("Hello from the daemon thread")
        time.sleep(2)

      

t1=threading.Thread(target=hello,daemon=True)
t1.start()

time.sleep(5)
print("main existing")