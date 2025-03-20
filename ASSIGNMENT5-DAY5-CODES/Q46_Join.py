# 46. Write a Python program that starts multiple threads, and ensure the 
# main thread waits for all threads to complete using the join() method. 


import threading
import time



def number():
        
    for i in range(1,6):
                print(i,"running")
                time.sleep(2)


t1=threading.Thread(target=number)

t1.start()
t1.join()


print("mai thread nowexciting")


                   