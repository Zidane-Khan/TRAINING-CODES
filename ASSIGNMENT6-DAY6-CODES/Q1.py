# For each enqueue operation print the new size of the queue. 

#  And for each dequeue operation print two integers, deleted element (-1, if queue is empty) and the new size of the queue. 

#  Sample Input 1  

#  5 

# E 2 

# D 

# D 

# E 3 

# D 

# Sample Output 1 

#  1 

# 2 0 

# -1 0 

# 1 

# 3 0 


#  5 

# E 2 

# D 

# D 

# E 3 

# D 



NUM=[]
QUEUE=[]

N=int(input("how many opration youwant to perform"))


for i in range(N):
    OPERATION = input("Enter operations: ")
    OPR1 = OPERATION.split(" ")
    # for i in OPR1:
    #     if i.isdigit():  # Corrected the method call by adding parentheses
    #         NUM.append(i)
    # print(NUM)
    # for i in OPR1:

    if  OPR1[0]=="E":
        num=int(OPR1[1])
       
        QUEUE.append(num)
        print(len(QUEUE))
    elif OPR1[0]=="D":
        if not QUEUE:
            print(-1,0) 
            
        else:   
            print(QUEUE[0])
            QUEUE.pop(0) 
            
        
        
      
    


# for i in range(len(n)):
#     if n: 
#         print("E", n[0])  
#         n.pop(0)  # Remove the first element
#     if not n:
#         print("D", -1)  # If the list is empty, print -1
#     else:
#         print("D", n)
#         print(len(n))

# print(n)
