# Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

total_amount = 0

ticket_price = float(input("Enter ticket amount per person: "))

for i in range(1, 6):
    age = int(input(f"Enter age of person {i}: "))

    if age < 12:
        amount = ticket_price * 0.70   # 30% discount
    elif age > 59:
        amount = ticket_price * 0.50   # 50% discount
    else:
        amount = ticket_price          # full price

    total_amount += amount

print("Total ticket amount for all 5 people =", total_amount)
