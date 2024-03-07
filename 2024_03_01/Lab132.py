# multiple exception
# try, except, finally
try:
    num1 = int(input("Enter a number : "))
    num2 = int(input("Enter a number : "))
    result = num1/num2 # ZeroDivisionError should be thrown when divisor is 0

except ValueError as v:
    print(v)
except ZeroDivisionError as z:
    print(z)
else:
    print(f"Div is {result}")
finally:
    print("This will execute with oe without an error.")