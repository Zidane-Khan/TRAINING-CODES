# 23. Write a Python class Product with a private attribute _price. Implement a 
# getter and setter method to access and modify the price, ensuring the price 
# cannot be set to a negative value. 


class Product:
    def __init__(self, price):

        if price < 0:
            print("Price cannot be negative")
        self._price = price
    
    
    def get(self):
        return self._price


    def set(self, price):
        if price < 0:
            print('No negative value should be there')
        else:
            self._price = price

obj = Product(99)


obj.set(56)


result = obj.get()

print(result)



