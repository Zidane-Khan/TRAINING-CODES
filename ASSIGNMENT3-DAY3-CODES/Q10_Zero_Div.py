# Write a Python program to handle the "ZeroDivisionError" exception and print a custom error message.
# Write a Python program to handle multiple exceptions (e.g., "FileNotFoundError" and "TypeError") and print custom error messages for each.


try :
    # raise ("THIS IS RAIUSE")
    NUM=10
    print(NUM/0)
    

except ZeroDivisionError:
    print(" NUM Cant divide by 0")

# except :
#     print("this is second")

# except ZeroDivisionError:
#     print("Cant divide by 0")

# else:
#     print("ELSE THIS")
finally:

    print("Error has been raised succesfully")