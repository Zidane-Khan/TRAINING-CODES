
# 1. Write a Python function that compresses a string such that repeated characters are replaced by the character followed by the count of occurrences. For example, the string "aaabbbcc" should become "a3b3c2". If the compressed string is not shorter than the original string, return the original string.
# a. Example Input: "aabbbcccc"
#      Expected Output: "a2b3c4"
# b. Example Input: "abc"
#      Expected Output: "abc" 
def compress():

    String1="aabbbcccc"
    output=String1[0]
    count=1

    for i in range(1,len(String1)):
        if String1[i]==String1[i-1]:
            count=count+1
        else:
            output+=str(count)+String1[i]
            count=1
    output+=str(count)
    print(output)

compress()

# 2. Write a Python function that finds the length of the longest substring without repeating characters in a given string.
# a. Example Input: "abcabcbb"
#  Expected Output: 3 (The longest substring is "abc")

S="kartik"
S1=list(S)
S2=[]

for i in S1:
    if i not in S2:
        S2.append(i)

print(len(S2))
print("".join(S2))


# a2b3c4
# # 3, abc
# both questions output



# 5. Write a function that attempts to open a file, read its content, and parse it into an integer. Handle the following exceptions:
# If the file is not found, catch FileNotFoundError and return "File not found."
# If the content is not a valid integer, catch ValueError and return "Invalid data in file."
# For any other exception, return "An error occurred during file processing."

try:

    MY_file='C:\\Users\\Zidane Khan\\Downloads\\SRFILE.txt'

    with open (MY_file,'r') as file:
        contents=file.read()
        print(contents)

except(FileNotFoundError):
    print('your file has not been found')

finally:
    print('first statement done')

try:

    MY_file='C:\\Users\\Zidane Khan\\Downloads\\SRFILE.txt'

    with open (MY_file,'r') as file:
        contents=file.read()
        print(contents)
        parse=int(contents)
        print(parse)  # this will throw and error invalid int

except(ValueError):
    print('Inavlid Data in file')


finally:
    print('Second  statement done')


# 3. Create a BankAccount class with the following methods:
# deposit(amount): Adds money to the balance.
# withdraw(amount): Subtracts money from the balance.
# get_balance(): Returns the current balance.

# class BankAccount:
     

#     # def __init__(self,balance):
#     #     self.balance=0
    
#     def deposit(amount):
#         balance=0
#         balance=balance+amount


#     def withdraw(amount):
#         balance=2000
#         balance=balance-amount

#     def get_balance(balance):
#         print(balance) 

# # balance=0
# obj=BankAccount
# obj.deposit(2000)
# obj.withdraw(1000)
# obj.get_balance(1000)


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):

        self.balance = self.balance+amount

    def withdraw(self, amount):

        self.balance = self.balance-amount
        

    def get_balance(self):
      
        return self.balance


account = BankAccount()  
account.deposit(2000)     
account.withdraw(1000)    # Withdraw 1000.
print(account.get_balance())  # 1000.




# 6. Write a Python function that merges the contents of multiple text files into a single file. 
# Each file's content should be appended to the output file, and each file's content should start on a new line.

TEXT='merge'  # this willmere

MY_file='C:\\Users\\Zidane Khan\\Downloads\\SRFILE.txt'

with open (MY_file,'a') as file:
    contents=file.write(TEXT)


with open (MY_file,'r') as appe_file:
    contents1=appe_file.read()
    print(contents1)


# output -zidanej723@gmail.commergemerge



