# Convert distance given in feet and inches into meter and centimeter.
#1 foot = 30.48 cm
#1 inch = 2.54 cm
#1 meter = 100 cm

# take input
feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))

# Convert feet and inches to centimeters
total_cm = feet * 30.48 + inches * 2.54

# Convert centimeters to meters and remaining centimeters
meters = int(total_cm // 100)
centimeters = total_cm % 100

#print("Distance in meters and centimeters:")
print(f"{meters} meter and {centimeters} centimeter")