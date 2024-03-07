# Using Try and Except

try:
    with open("TestData.txt", 'r') as file:
        content = file.read()
        print(content)
        file.close()
except Exception as e:
    print(e)