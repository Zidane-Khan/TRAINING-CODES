# 	Write a function that finds the common elements between two lists and returns them as a list.



def Common(LIST1,LIST2):


    LiST3=[]
    for i in LIST1:
        for j in LIST2:
            if i==j:
                LiST3.append(i)
    print(LiST3)


Common([3,4,2,1],[2,3,5,6])
