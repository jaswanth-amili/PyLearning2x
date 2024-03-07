name = "Hanuman"

print(len(name))

print(name[5])

# If we try to print more than the length of string we get Index out of Error
# print(name[9])

print(name[len(name) -1])

# Strings are immutable
name[2] = "l"

# We can change the entire value of the variable name
name = "Jack"
