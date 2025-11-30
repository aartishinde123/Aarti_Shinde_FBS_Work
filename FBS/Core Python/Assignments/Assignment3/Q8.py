# Write a program to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the same. If user enters the same number then show him success message otherwise failed. (Something like captcha)

import random

# Step 1: Correct login details
correct_userid = "admin"
correct_password = "1234"

# Step 2: Ask user for login details
userid = input("Enter User ID: ")
password = input("Enter Password: ")

# Step 3: Verify login
if userid == correct_userid and password == correct_password:
    # Generate 4 digit random number
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)

    # Step 4: Ask user to enter captcha
    user_input = int(input("Enter the above number: "))

    if user_input == captcha:
        print("Login Successful.")
    else:
        print("Captcha Incorrect Login Failed.")
else:
    print("Invalid User ID or Password")
