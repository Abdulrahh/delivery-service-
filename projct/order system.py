from canteen import order_food

def delivery_options():
    while True:
        choice = input("Do you want delivery or pickup? ").lower().strip()
        if choice == "delivery":
            address = input("Enter Address for delivery: ")
            if address == "":
                print("please enter a valid address")
                continue
            print(f"Your order will be deliveried to this Address {address}")
            return "delivery", address
        elif choice == "pickup":
            print("You have chosen to pick up your order.")
            return "Pickup", None
        else:
            print("Please type 'delivery' or 'pickup'.")

def main():
    name, cart, total = order_food()
    if cart:  
        method, address = delivery_options()
        print("------ ORDER SUMMARY ------")
        print(f"Name: {name}")
        print("Items:", ", ".join(cart))
        print(f"Total: £{total:.2f}")
        print(f"Method: {method}")
        if address:
            print(f"Address: {address}")
        print("----------------------------")
        print("Thank you for your order!")

if __name__ == "__main__":
    main()