# 53. Write a Python program that simulates a thread communication 
# mechanism using Condition variables. One thread waits for a condition 
# to be met before proceeding, while another thread signals the 
# condition. 

import threading
import time

condition=threading.Condition()
share=None

def wait_thread():
    global share
    with condition:
        print("waiting for condition")
        condition.wait()
        print(f"condition met, {share}")

def signal():
    global share
    time.sleep(2)
    with condition:
        share='ready data'
        condition.notify()

ti=threading.Thread(target=wait_thread)
t2=threading.Thread(target=signal)

ti.start()
t2.start()
ti.join()
t2.join()
