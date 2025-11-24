#Write a program to enter P, T, R and calculate simple Interest.

# Taking inputs
P = int(input("Enter Principal amount : "))
T = int(input("Enter Time in years : "))
R = int(input("Enter Rate of Interest : "))

# Calculating Simple Interest
SI = (P * T * R) / 100

# Displaying the result
print("Simple Interest =", SI)