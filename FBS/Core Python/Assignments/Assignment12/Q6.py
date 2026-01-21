# Python Program to Take in a String and Replace Every Blank Space with Hyphen

string = input("Enter a string: ")

new_string = ""

for ch in string:
    if ch == " ":
        new_string = new_string + "-"
    else:
        new_string = new_string + ch

print("Modified string:", new_string)
