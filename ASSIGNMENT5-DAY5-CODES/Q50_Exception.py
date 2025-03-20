# 50. Write a Python program where a thread raises an exception. Handle the 
# exception in the main thread and print an appropriate error message. 

import threading

exception=None

def raise_error():


    global exception
    
    try:
        raise ValueError(" error thread")
    except Exception as e:
        exception=e

t1=threading.Thread(target=raise_error)
t1.start()
t1.join()

if exception:
    print("Error caught", exception)



