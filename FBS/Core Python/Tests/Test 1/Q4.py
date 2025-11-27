area = int(input("Enter area of one wall: "))
interior_cost = int(input("Enter cost per sq unit for interior wall: "))
exterior_cost = int(input("Enter cost per sq unit for exterior wall: "))

# Walls count
interior_walls = 8     # 4 walls per room, 2 rooms → 8 interior
exterior_walls = 7     #  1 wall is common

# Calculate costs
total_interior_cost = interior_walls * area * interior_cost
total_exterior_cost = exterior_walls * area * exterior_cost

total_cost = total_interior_cost + total_exterior_cost

# display result
print("Total interior painting cost =", total_interior_cost)
print("Total exterior painting cost =", total_exterior_cost)
print("Total painting cost =", total_cost)