# Fibonacci series

num = int(input("Enter a number : "))

a, b = 0, 1
if num <= 0:
    print("Enter valid number")
else:
    while a < num:
        print(a, end=" ")
        a,b = b, a+b
