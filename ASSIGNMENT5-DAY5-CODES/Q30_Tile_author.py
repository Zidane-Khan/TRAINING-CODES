# 30. Write a Python class Book that has attributes title and author. Implement 
# the __eq__ method to compare two Book objects for equality based on their title and author.


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

obj1 = Book("Zidane", "Code")
obj2 = Book("Zidane", "Code")
obj3 = Book("Khan", "pyrhon")

print(obj1 == obj2)
print(obj1 == obj3)
