#Define menu in dictionary
menu={
    'Pasta': 50,
    'Pizza': 100,
    'Salad': 70,
    'Burger': 120,
    'Coffee': 90
}

#Greeting
print("Welcome to Python Restaurant!")
print("Here is our menu:")
# for item in menu:
#     print(item)
print("Pasta : Rs.50\nPizza: Rs.100\nSalad : Rs.70\nBurger: Rs.120\nCoffee :Rs.90")

order_total=0
#Ask user for order
item_1=input("Please enter item name from menu: ")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet!")

another_order=input("Do you want to order another item? (yes/no) ")
if another_order.lower() == 'yes':
    item_2=input("Please enter item name from menu: ")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available yet!")

print(f"The total amount of items to pay is Rs.{order_total}")