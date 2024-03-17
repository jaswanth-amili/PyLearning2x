# Continue

for i in range(1,10):
    if  i % 2 == 0:
        print("Even number ", i)
    else:
        print("Odd number ", i)
print("------------------------------------------")
for i in range(1,10):
    if  i % 2 == 0:
        print("Even number ", i)
        continue
    print("Odd number ", i)

