# Write a program to convert days into years, weeks and days.

# Taking input 
days = int(input("Enter number of days: "))

# Calculations
years = days // 365              # 896 // 365 = 2
remaining_days = days % 365      # 896 % 365 = 23
print(remaining_days)
weeks = remaining_days // 7      # 23 // 7 =
days_left = remaining_days % 7

# Displaying result
print("Years:", years)
print("Weeks:", weeks)
print("Days:", days_left)