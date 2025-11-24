# WAP to calculate area of triangle and rectangle

# Triangle area
# take input
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
# calculating area
triangle_area = 0.5 * base * height

# Rectangle area
# take input
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
# calculating area
rectangle_area = length * breadth

# dislaying result
print("Area of Triangle =", triangle_area)
print("Area of Rectangle =", rectangle_area)