# Task #Week 1
"""
Task #1 - Take a user input (name, age, roll_number, phone_number) and print the user details.
"""
name = input("Enter name : ")
age = input("Enter age : ")
roll_number = input("Enter roll : ")
phone_number = input("Enter phone number : ")

print(name, age, roll_number, phone_number, sep='\n')

"""
Task #2 - Print the Table of 2 by using the command print()
2 x 1 = 2
2 x 2 = 4
...
2 x 10 = 20
Use printf command
"""
num = 2
print(
    f"\n{num} X 1 = {num}\n{num} X 2 = {num*2}\n{num} X 3 = {num*3}\n{num} X 4 = {num*4}\n{num} X 5 = {num*5}\n{num} X 6 = {num*6}\n"
    f"{num} X 7 = {num*7}\n{num} X 8 = {num*8}\n{num} X 9 = {num*9}\n{num} X 10 = {num*10}")
