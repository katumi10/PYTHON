# Exercise 2: shopping cart program


item = input("What would you like to buy: ")
price = float(input("What is the price: "))
quantity = int(input("How many would you like to buy: "))
total = price * quantity

print(f"Your items cost ${total}")