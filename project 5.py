# HOTEL MENU
# Define the menu of restaurant
menu ={
    'Pizza': 60,
    'Burger':40,
    'Coffee':50,
    'Salad' :70,
    'Pasta': 90,
    'Samosa':20,
    'Cold drink':40,
}

print("Welcome to my restaurant")
print("Pizza : Rs60\nBurger : Rs40\nCoffee : Rs50\nSalad : Rs70\nPasta : Rs90\nSamosa: Rs20\nCold drink: Rs40\n")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No)")    
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print("Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The total amount of items to pay is {order_total}")        