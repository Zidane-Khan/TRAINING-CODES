# 4. Write a Python program that creates a custom thread class by 
# subclassing the Thread class. The thread should print a message 
# indicating the current thread’s name and ID. 

import threading

class Customthread (threading.Thread):
    def current(self):
        print(f"Name:{self.name}, id:{threading.get_ident()}")

t1=Customthread()
t1.start()
t1.join()