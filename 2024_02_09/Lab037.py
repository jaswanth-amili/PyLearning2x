# Find max between 3 numbers

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
num3 = int(input("Enter num3 : "))

max_num = max(num1, num2, num3)
print(max_num)

if num1 > num2 and num1 > num3:
    print(num1, "is max")
elif num2 > num1 and num2 > num3:
    print(num2, "is max")
elif num3 > num2 and num3 > num1:
    print(num3, "is max")
else:
    print("Some might be equal")