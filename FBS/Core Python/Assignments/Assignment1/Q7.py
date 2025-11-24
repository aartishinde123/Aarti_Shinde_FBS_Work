# Program to Find the Roots of a Quadratic Equation

# Taking input
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = b*b - 4*a*c     # Discriminant

# calculating the roots

root1 = (-b + d**0.5) / (2*a)
root2 = (-b - d**0.5) / (2*a)
print("Root 1 =", root1)
print("Root 2 =", root2)