# Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

amount = int(input("Enter amount: "))

notes = [2000,500,200,100,50,20,10]

tn = amount//2000
amount = amount%2000
print(tn)
fiven = amount//500
amount = amount%500

twon = amount//200
amount = amount%200
print(twon)
onen = amount//100
amount = amount%100

fiftyn = amount//50
amount = amount%50

twentyn = amount//20
amount = amount%20

tenn = amount//10
amount = amount%10

total_notes = tn + fiven + twon + onen + fiftyn + twentyn + tenn

print("Minimum number of notes:",total_notes)


