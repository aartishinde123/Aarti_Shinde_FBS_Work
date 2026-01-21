# Python Program to Form a New String where the First Character and the Last Character have been Exchanged

string = input("Enter a string: ")

# If string length is 1 or empty, no change
if len(string) <= 1:
    print("New string:", string)
else:
    new_string = string[-1]      # last character

    for i in range(1, len(string) - 1):
        new_string = new_string + string[i]

    new_string = new_string + string[0]   # first character

    print("New string:", new_string)
