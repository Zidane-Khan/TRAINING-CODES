# 8. Write a Python program where one thread generates numbers from 1 to 
# 10 and places them in a Queue, and another thread retrieves and prints 
# those numbers from the Queue. 


import threading
import time
import queue


que=queue.Queue()

def generator():
    for i in range(1,6):
        que.put(i)
        print(f"produce {i}")
        time.sleep(1)

def retrieves():
    for i in range(1,6):
        num=que.get()
        print(f"retriev {num}")
        time.sleep(1)

ti=threading.Thread(target=generator)
t2=threading.Thread(target=retrieves)

ti.start()
t2.start()

ti.join()
t2.join()


print("exiting")