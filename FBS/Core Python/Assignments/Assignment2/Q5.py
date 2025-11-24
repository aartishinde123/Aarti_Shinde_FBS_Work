# WAP to calculate selling price of book based on cost price and discount.

# take input
cost_price = int(input("Enter cost price of the book: "))
discount = int(input("Enter discount percentage: "))

# calculate selling price
selling_price = cost_price - (cost_price * discount / 100)

# display result
print("Selling Price of the book =", selling_price)