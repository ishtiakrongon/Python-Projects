# CONCESSION STAND PROGRAM

menu = {
    'pizza': 3.00,
    'nachos': 4.50,
    'popcorn': 6.00,
    'fries': 2.50,
    'chips': 1.00,
    'pretzel': 3.50,
    'soda': 3.00,
    'lemonade': 4.25
}

cart = {}
total = 0

print("--------MENU--------")
for index, (key, value) in enumerate(menu.items(), start=1):
    print(f"{index}. {key:10}: {value:.2f}")
print(f"{'-'*20}")

while True:
    food = input("Select an item (q to quit): ").strip().lower()

    if food == 'q':
        break
    elif food in menu:
        if food in cart:
            cart[food] += 1
        else:
            cart[food] = 1
    else:
        print(f"Sorry, we don't have '{food}' on the menu. Please choose an item from the menu.")

print("\nItems in your cart:")
for food, quantity in cart.items():
    price = menu[food] * quantity
    total += price
    print(f"{food.capitalize()} x{quantity} - {price:.2f}")

print(f"\nTotal is: {total:.2f}.")
