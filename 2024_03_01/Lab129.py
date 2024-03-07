# Without Exception we get an error which not handled

num1 = int(input("Enter a number : \n"))
num2 = int(input("Enter a number : \n"))

c = num1/num2 # ZeroDivisionError should be thrown when divisor is 0

print("Div is ", c)
print("This is a message after division")
