class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    @classmethod
    def from_string(cls, book_string):
  
        title, author, isbn = book_string.split(",")

        return cls(title, author, isbn)
  
    @staticmethod
    def is_valid_isbn(isbn):
        
        if len(isbn) == 13 and isbn.isdigit():
            return True
        return False
    
    def display_info(self):
        # Display the book information
        print(f"Book Info: {self.title} by {self.author}, ISBN: {self.isbn}")



book1 = Book.from_string("The Great Gatsby,F. Scott Fitzgerald,9780743273565")
book1.display_info() 

print(Book.is_valid_isbn("9780743273565")) 
print(Book.is_valid_isbn("123456"))         
