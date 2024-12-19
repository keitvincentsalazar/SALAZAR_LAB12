# Food Ordering System

def display_menu():
    menu = {
        1: ("Burger", 4.99),
        2: ("Pizza", 10.99),
        3: ("Pasta", 8.49),
        4: ("Salad", 6.99),
        5: ("Soda", 0.99)
    }
    print("\nMenu:")
    for key, (item, price) in menu.items():
        print(f"{key}. {item} - ${price:.2f}")
    return menu

def get_order(menu):
    while True:
        try:
            choice = int(input("\nEnter the number of the item you'd like to order: "))
            if choice in menu:
                return menu[choice]
            else:
                print("Invalid choice. Please select a valid menu item.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def process_payment(total_cost):
    while True:
        try:
            cash = float(input(f"\nYour total is ${total_cost:.2f}. Enter payment amount: "))
            if cash >= total_cost:
                change = cash - total_cost
                print(f"Payment accepted. Your change is ${change:.2f}.")
                break
            else:
                print(f"Insufficient amount. You still owe ${total_cost - cash:.2f}. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid payment amount.")

def main():
    print("Welcome to the Food Ordering System!")
    menu = display_menu()
    item, price = get_order(menu)
    print(f"\nYou ordered: {item} - ${price:.2f}")
    process_payment(price)
    print("\nThank you for your order! Have a great day!")

if __name__ == "__main__":
    main()
