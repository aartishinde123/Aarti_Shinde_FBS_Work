# Write a Program to input two angles from user and find third angle of the triangle.

# Taking inputs
angle1 = int(input("Enter first angle: "))
angle2 = int(input("Enter second angle: "))

# calculating third angle
# Sum of angles of a triangle is always 180
angle3 = 180 - (angle1 + angle2)

# Display result
print("The third angle of the triangle is:", angle3)