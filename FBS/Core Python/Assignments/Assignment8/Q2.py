# Write a program to calculate area of circle

def area_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

r = float(input("Enter radius: "))

result = area_circle(r)

print("Area of circle:", result)
