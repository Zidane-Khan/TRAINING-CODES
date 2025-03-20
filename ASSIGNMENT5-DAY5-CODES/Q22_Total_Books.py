# 22. Create a class Book with a class attribute total_books that keeps track of the 
# total number of books created. Use this attribute to count the books as new 
# instances are created. 


# A class attribute in Python is a variable that belongs to a class rather than a specific object. It is shared 
# by all instances of the class and is defined outside the constructor function (init()).
#  You can access the value of a class attribute using class_name.class_attribute or object_name.class_attribute

class Book:

    total_books=0

    def book_key(book_key:int):
        

         if book_key:
            total_books+=1

         return book_key

obj=Book(1)
ob2=Book(2)


# A class attribute in Python is a variable that belongs to a class rather than a specific object. It is shared 
# by all instances of the class and is defined outside the constructor function (init()).
#  You can access the value of a class attribute using class_name.class_attribute or object_name.class_attribute

class Book:

    total_books=0

    def book_key(book_key:int):
        

         if book_key:
            total_books+=1

         return book_key

obj=Book(1)
ob2=Book(2)









    

