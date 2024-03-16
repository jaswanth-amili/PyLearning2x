# Program to calculate and display the letter grade for a given score i.e. A, B, C, D, or F
# Based on the following input:
# A : 90 - 100
# B : 80 - 89
# C : 70 - 79
# D : 60 - 69
# F : 0 - 59

score = int(input("Enter the marks : "))

if score >= 90 and score <= 100:
    print("Grade is A")
elif score >= 80 and score < 90:
    print("Grade is B")
elif score >= 70 and score < 80:
    print("Grade is C")
elif score >= 60 and score < 70:
    print("Grade is D")
else:
    print("Grade is F")