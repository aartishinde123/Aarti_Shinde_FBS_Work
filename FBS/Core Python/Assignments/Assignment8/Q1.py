#Write a program to calculate area of rectangle

def area_rectangle(length, width):
    area = length * width
    return area

l = int(input("Enter length: "))
w = int(input("Enter width: "))

result = area_rectangle(l, w)

print("Area of rectangle:", result)
