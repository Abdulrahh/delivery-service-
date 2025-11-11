def order_food():
    while True:
        name = input("Please enter your name: ")
        if name == "":
            print("Enter a valid!!")
        else:
            print(f"Welcome {name}")
            break

    menu = {"Veggie Burger": 5.50,
            "Chicken Warp": 6.20,
            "Large Fries": 3.00,
            "Soda": 1.75,
            "Apple Juice": 2.50}


    cart = []
    total = 0 


    print("----------MENU----------")
    for key, value in menu.items():
        print(F"{key:10}: {value:.2f}")
    print("-------------------------")


    while True:
        food = input("Select an Item from the menu(q to quit): ").title()
        if food == "Q":
            break 
        elif food in menu:
            cart.append(food)
        else:
            print("Item not found on the menu. Please try again.")


    for food in cart:
        total = total + menu.get(food)
        print(food, end=" ")
    print()
    print("----------YOUR ORDER ----------")
    print(F"Total is: £{total:.2f}")

    return name, cart, total

if __name__ == "__main__":
    order_food()
