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
print(
    f"\n{2} X {1} = {2}\n{2} X {2} = {4}\n{2} X {3} = {6}\n{2} X {4} = {8}\n{2} X {5} = {10}\n{2} X {6} = {12}\n"
    f"{2} X {7} = {14}\n{2} X {8} = {16}\n{2} X {9} = {18}\n{2} X {10} = {20}")
