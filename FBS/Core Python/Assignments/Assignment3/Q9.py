# Input 5 subject marks from user and display grade(eg.First class,Second class ..)

# Input 5 subject marks
m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))
m5 = float(input("Enter marks of subject 5: "))

# Calculate total and percentage
total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("Percentage =", percentage)

# Decide grade
if percentage >= 75:
    print(" Distinction")
elif percentage >= 60:
    print(" First Class")
elif percentage >= 45:
    print(" Second Class")
elif percentage >= 35:
    print(" Pass")
else:
    print(" Fail")
