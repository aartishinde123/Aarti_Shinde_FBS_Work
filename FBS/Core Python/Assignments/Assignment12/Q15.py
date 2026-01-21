# Python Program to find larger string without using built-in functions.

# Take two strings from user
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Count length of first string
count1 = 0
for ch in str1:
    count1 += 1

# Count length of second string
count2 = 0
for ch in str2:
    count2 += 1

# Compare lengths
if count1 > count2:
    print("Larger string is:", str1)
elif count2 > count1:
    print("Larger string is:", str2)
else:
    print("Both strings are of equal length")
