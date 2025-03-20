# 3. Write a Python class MyList that implements the __getitem__ and 
# __setitem__ methods. 


# __setitem__ is a method used for assigning a value to an item. It is implicitly invoked when we 
# set a value to an item of a list, dictionary, etc. 
# __getitem__ is a method used for getting 
# the value of an item. It is implicitly invoked when we access the items of a list, dictionary, etc.



  

class MyList:

    def __getitem__(self,value):
        print(type(value),value)

    def __setitem__(self,key,value):
        print(f" set {value} for {key}")
        return key


    
    # def __setitem__():

mylist=MyList()
mylist["Zzidane"]="Khan"
print(mylist["Zidane"])




