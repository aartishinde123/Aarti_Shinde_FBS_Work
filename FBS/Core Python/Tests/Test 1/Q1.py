length = int(input('Enter length: '))
breadth = int(input('Enter breadth: '))
radius = int(input('Enter radius: '))

rectangle_area = length * breadth
semicircle_area = 0.5 * 3.14 * radius * radius

rectangle_perimeter = 2 * (length + breadth)
semicircle_perimeter = 3.14 * radius + 2 * radius

Total_Area = rectangle_area + semicircle_area
Total_Perimeter = rectangle_perimeter + semicircle_perimeter

print('Total area of figure:', Total_Area)
print('Total perimeter of figure:', Total_Perimeter)
