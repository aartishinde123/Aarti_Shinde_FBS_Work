#Accept no. of passengers from user and per ticket cost. Then accept age of each passenger and then calculate total amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

n = int(input("Enter number of passengers: "))
cost = float(input("Enter ticket cost: "))

total_amount = 0

for i in range(1, n + 1):
    age = int(input("Enter age of passenger " + str(i) + ": "))

    if age < 12:
        amount = cost * 0.70   # 30% discount
    elif age > 59:
        amount = cost * 0.50   # 50% discount
    else:
        amount = cost          # full payment

    total_amount += amount

print("Total ticket amount =", total_amount)
