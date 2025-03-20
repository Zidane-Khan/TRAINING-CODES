# 51. Write a Python program that uses a timer thread to execute a function 
# after a delay of 5 seconds. The function should print "Timer expired". 


import threading
import time

def delay():
    print("Timer expired")

timer=threading.Timer(5,delay)
timer.start()