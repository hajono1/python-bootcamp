# How many items to purchase
item_count = int(input("Enter item count: "))
total = 0

for item in range(item_count):
    item_quantity = int(input("Enter item quantity: "))
    item_price = int(input("Enter item price: "))
    item_subtotal = item_quantity * item_price 
    total = total + item_subtotal
print(total)
