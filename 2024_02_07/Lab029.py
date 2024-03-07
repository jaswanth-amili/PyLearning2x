# String concat

str1 = "Jack"
str2 = "sparrow"
str3 = str1 + str2
print(str3)

# print(str1 + 1) # TypeError: can only concatenate str (not "int") to str
print(str1 + str(1))


str4 = "Hello "
str4 += "World"
print(str4)

# Not allowed to do ++ and -- in Python

x = 5
x += 1