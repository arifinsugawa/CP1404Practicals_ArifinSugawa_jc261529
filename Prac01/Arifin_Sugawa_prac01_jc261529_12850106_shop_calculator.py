"""
Shop Calculator
The output should look something like (bold text represents user input):
Number of items: 3
Price of item: 100
Price of item: 35.56
Price of item: 3.24
Total price for 3 items is $124.92
+ Error checking (input validation loop):
(Do this after you have completed the above program.)
If the number of items is less than zero, the message "Invalid number of items!" should be displayed and this quantity must be re-entered by the user until it is valid.
"""
total_price = 0
item_prices = []
count = 1
amount_items = int(input("Input the amount of items for checking out: "))
while amount_items < 0:
    amount_items = int(input("Amount of items must be more than 0. Please Input again! "))

for i in range(1, amount_items + 1):
    item_price = float(input("Input the price of the item {}: ".format(i)))
    item_prices.append(item_price)
    total_price = total_price + item_price

for i in item_prices:
    print("Price for the item {}: ${}".format(count, item_prices[count - 1]))
    count += 1
if total_price > 100:
    total_price = total_price - (total_price * 0.10)
else:
    pass

print("The total price for {} items is ${}".format(amount_items, total_price))