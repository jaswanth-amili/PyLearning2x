# Leap year checker
yr = int(input("Enter year : "))
if (yr % 400 == 0) or ((yr % 4 == 0) and (yr % 100 != 0)):
    print(yr, "is a leap year")

# Triangle classifier
s1 = int(input("Enter side 1 : "))
s2 = int(input("Enter side 2 : "))
s3 = int(input("Enter side 3 : "))

if s1 == s2 == s3:
    print(" This is a equilateral triangle")
elif s1 == s2 or s1 == s3 or s2 == s3:
    print("This is an isosceles triangle")
else:
    print("This is a scalene triangle")
