#Define the menu of restaurant
menu ={
    'Pizza':40,
    'Burger':30,
    'Sandwich':25,
    'Fries':15,
    'Soda':10,
    'Water':5

}
#Greet
print("Welcome to our restaurant!")
print("Here is our menu:")
print('Pizz: Rs40')
print('Burger: Rs30')
print('Sandwich: Rs25')
print('Fries: Rs15')
print('Water: Rs10')

#Get order
order_total = 0

while True:
    item_1= input("What would you like to order? (or 'done' to finish):")
    if item_1 in menu:
        order_total += menu[item_1]
        print(f"Your item {item_1} has been added to your order")
    else:
        print(f"Ordered item {item_1} is not avaialable yet")

    another_order = input("Do you want to add another item?(yes/no)")
    if another_order.lower() == 'yes':
        item_2 = input("Enter the name of second item = ")
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"Your item {item_2} has been added to your order")
        else:
            print(f"Ordered item {item_2} is not available yet")
    print(f"The total amount of items to pay is {order_total} ")
    print("Thank you  for your order !!!...")


    