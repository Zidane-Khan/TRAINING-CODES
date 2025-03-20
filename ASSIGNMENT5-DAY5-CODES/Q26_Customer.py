# 26. Create a class Customer that represents a customer in a store with 
# attributes like name, address, and phone_number. Include methods for 
# updating the customer details.

class Customer:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number

    # def update_name(self, new_name):
  
    #     self.name = new_name
    #     print(f"Name updated to: {self.name}")

    # def update_address(self, new_address):
    #     self.address = new_address
    #     print(f"Address updated to: {self.address}")

    # def update_phone_number(self, new_phone_number):
    #     self.phone_number = new_phone_number
    #     print(f"Phone number updated to: {self.phone_number}")

    def display(self):
        print(f"Customer Info:\nName: {self.name}\nAddress: {self.address}\nPhone Number: {self.phone_number}")


obj = Customer("Zidanme", "KALWad", 777)

obj.display()

# obj.update_name("khan")
# obj.update_address("Lohgaon")
# obj.update_phone_number(99)

# obj.display()

