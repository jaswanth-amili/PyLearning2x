# Strings are sequence of characters

name1 = "Jack"
name2 = 'Sparrow'

print(type(name1))

# To ignore the escape characters we should use \\
print("C:\nalder\software")
print("C:\\nalder\software")

# Raw string ignores the escape characters
print("Raw string ignores the escape characters")

print(r"C:\nalder\software")

# Format string
f_name = "Jack"
l_name = "sparrow"
age = 28
isMarried = False
print(f"Your name is {f_name} {l_name} of age {age}. Your marital status is {isMarried}")