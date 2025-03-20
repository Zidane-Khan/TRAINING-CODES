# 55. Write a Python program where one thread generates random numbers, 
# and another thread prints the numbers. Use an Event object to 
# synchronize the printing when a new number is generated. 


import threading
import random
import time

event=threading.Event()
random_no=None
def gen_num():
    global random
    for i in range(6):
        time.sleep(2)
        random_no=random.randint(1,50)
        print("Generated,{random_no}")
        event.set()
        event.clear()

def print():
    for i in range(6):
        event.wait()
        print("printed,{random_no}")


ti=threading.Thread(target=gen_num)
t2=threading.Thread(target=print)

ti.start()
t2.start()
ti.join()
t2.join()
