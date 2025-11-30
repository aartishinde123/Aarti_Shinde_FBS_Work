# Write a program to input any alphabet and check whether it is vowel or consonant.

ch = input("Enter any alphabet: ")

if ch in 'aeiouAEIOU':
    print(ch, "is a vowel")
else:
    print(ch, "is a consonant")    