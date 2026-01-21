# Python Program to Count the Number of Vowels in a String

string = input("Enter a string: ")

count = 0

for ch in string:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' \
       or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
        count = count + 1

print("Number of vowels:", count)
