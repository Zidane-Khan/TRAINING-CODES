# 45. Write a Python program that creates two threads. One thread should 
# print the numbers from 1 to 5, and the other thread should print the 
# letters from 'A' to 'E'. Use the threading module. 

import threading
import time

def number():
    for i in range(1,6):
        print(i)
        time.sleep(2)
                   
def letter():
    for i in 'abcde':
        print(i)
        time.sleep(2) 

ti=threading.Thread(target=number)
t2=threading.Thread(target=letter)

ti.start()
t2.start()
ti.join()
t2.join()


print("finished ")


