#price notification template
price_notification = "The price of {coffee} is ${price}."

print(price_notification.format(coffee = "latte", price = "3.50"))
print(price_notification.format(coffee = "Espresso", price = "2.75"))
print(price_notification.format(coffee = "Cappuccino", price = "4.00"))
