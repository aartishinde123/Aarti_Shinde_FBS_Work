# A farmer has a field which is half in circle share and rest rectangle. 
# He needs to do fencing for entire field using barbed wire 5 times. 
# Circular section has radius 20m and rectangle length is 50 m and breadth is 40m. 
# If cost of barbed wire is 35Rs/m then calculate the total cost of fencing the field.

length = int(input("Enter length:"))
breadth = int(input("Enter breadth:"))
radius = int(input("Enter radius:"))
cost = int(input("Enter the cost of barbed wire per meter:"))

area_semicircle = 0.5 * 3.14 * radius * radius
area_rectangle = length * breadth
total_area = area_semicircle + area_rectangle
total_wire = 5 * total_area
cost = 35 * total_wire
print("total cost of fencing the field is :",cost)