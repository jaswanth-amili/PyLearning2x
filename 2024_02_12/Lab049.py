# Factorial
num = int(input("Enter the number : "))

if num < 0:
    print("Enter a valid number")
elif num ==0:
    print("Factorial is 1")
else:
    fact = 1
    for i in range(2,num+1):
        fact *= i
print(fact)
