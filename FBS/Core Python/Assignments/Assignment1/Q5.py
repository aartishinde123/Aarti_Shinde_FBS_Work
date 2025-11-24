# Write a program to enter P, T, R and calculate Compound Interest.

# Taking inputs
P = int(input("Enter Principal amount : "))
T = int(input("Enter Time in years : "))
R = int(input("Enter Rate of Interest : "))

# Calculating Compound Interest
A = P * (1 + R/100) ** T   # Final amount
CI = A - P                 # Compound Interest

# Displaying results
print("Final Amount :", A)
print("Compound Interest :", CI)