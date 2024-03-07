# File handling
# How to read and write text from a file using python

# Select Function:
# open("file_name", "mode")

# Select Mode:
# 'r' for reading (default)
# 'w' write
# 'a' append



# Close the file

file = open("TestData.txt", 'r')
content = file.read()
print(content)
file.close()
