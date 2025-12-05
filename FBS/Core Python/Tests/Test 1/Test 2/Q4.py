#Write a program to calculate the total cost of painting. The interior of building with four equal sized walls.

height = int(input("Enter height of each wall (in meters): "))
width = int(input("Enter width of each wall (in meters): "))
cost = int(input("Enter painting cost per square meter: "))

# Area of 1 wall
area_one_wall = height * width

# Total area of 4 walls
total_area = area_one_wall * 4

# Total cost
total_cost = total_area * cost

print("Total area to be painted =", total_area)
print("Total painting cost =", total_cost)
