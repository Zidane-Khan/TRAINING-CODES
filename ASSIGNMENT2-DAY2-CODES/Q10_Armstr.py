# number to check if it is an Armstrong number:

num = int(input("Enter a number to check if it is an Armstrong number: "))
num_str = str(num)
num_digits = len(num_str)
total = 0
for digit in num_str:
    total += int(digit) ** num_digits
if total == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
