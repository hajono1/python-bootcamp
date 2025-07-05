item_1_price = int(input("Input your item price 1:"))
item_2_price = int(input("Input your item price 2:"))
item_3_price = int(input("Input your item price 3:"))

#quantity of each item
item_1_quantity = int(input("How many of item 1 did you buy?:"))
item_2_quantity = int(input("how many of item 2 did you buy?:"))
item_3_quantity = int(input("how many of item 3 did you buy?:"))

item_1_total = item_1_price * item_1_quantity
item_2_total = item_2_price * item_2_quantity
item_3_total = item_3_price * item_3_quantity

#print total cost
total = item_1_total + item_2_total + item_3_total
print(total)
