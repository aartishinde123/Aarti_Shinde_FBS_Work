# A man goes for shopping. He buys 5 products. Accept the price of all products and display the total bill after adding 18% GST

p1 = int(input("Enter the cost of first product:"))
p2 = int(input("Enter the cost of second product:"))
p3 = int(input("Enter the cost of third product:"))
p4 = int(input("Enter the cost of fourth product:"))
p5 = int(input("Enter the cost of fifth product:"))

bill = p1 + p2 + p3 + p4 +p5
total_bill = bill + ( bill*0.18)
print(" Total Bill =",total_bill)