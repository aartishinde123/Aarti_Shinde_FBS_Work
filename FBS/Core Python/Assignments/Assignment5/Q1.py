#Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter the credentials. Let him try 3 times. After that program to terminate.

uid = "admin"
pwd = "123"

for i in range(3):
    user = input("Enter user id: ")
    password = input("Enter password: ")

    if user == uid and password == pwd:
        print("Login successful")
        break
    else:
        print("Wrong id or password")

if user != uid or password != pwd:
    print("Program terminated")
