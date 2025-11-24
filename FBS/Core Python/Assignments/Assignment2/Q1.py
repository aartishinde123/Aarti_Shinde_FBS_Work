#WAP to Convert the time entered in hh,min and sec into seconds.

# Input values
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

# Calculating total seconds
total_seconds = hours * 3600 + minutes * 60 + seconds

# Display Output
print("Total seconds:", total_seconds)