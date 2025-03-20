# ⦁Write a Python program that iterates the integers from 1 to 50. 
# For multiples of three print "Fizz" instead of the number and for multiples of five print 
# "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".


NO = 50

for i in range(1, NO + 1):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
        
print('HERE ARE YOUR MULTIPLES')