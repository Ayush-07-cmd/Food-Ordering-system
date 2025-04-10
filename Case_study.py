menu = {
    1: {'name': 'Pizza', 'price': 12.99},
    2: {'name': 'Burger', 'price': 8.99},
    3: {'name': 'Pasta', 'price': 10.99},
    4: {'name': 'Salad', 'price': 7.99},
    5: {'name': 'Soda', 'price': 1.99}
}
orders = []

def display_menu():
    print("\n--- Menu ---")
    for item_id, item in menu.items():
        print(f"{item_id}. {item['name']} - ${item['price']:.2f}")

def place_order():
    display_menu()
    while True:
        try:
            choice = int(input("Select an item number to order (0 to finish): "))
            if choice == 0:
                break
            elif choice in menu:
                quantity = int(input(f"How many {menu[choice]['name']}s would you like to order? "))
                total_price = menu[choice]['price'] * quantity
                orders.append((menu[choice]['name'], quantity, total_price))
                print(f"Added {quantity} {menu[choice]['name']}(s) to your order.")
            else:
                print("Invalid item number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def apply_discount(total_amount, discount_percentage):
    discount_amount = total_amount * (discount_percentage / 100)
    return total_amount - discount_amount

def confirm_order():
    if not orders:
        print("No items in your order.")
        return

    print("\n--- Your Order ---")
    total_amount = 0
    for item, quantity, total in orders:
        print(f"{item} (x{quantity}) - ${total:.2f}")
        total_amount += total

    discount_code = input("Enter discount code (if any): ").strip()
    if discount_code == "SAVE10":
        total_amount = apply_discount(total_amount, 10)
        print("Discount applied: 10% off!")
    else:
        print("No discount applied." if discount_code == "" else "Invalid discount code.")

    print(f"\nTotal Amount: ${total_amount:.2f}")
    confirm = input("Do you want to confirm your order? (yes/no): ").strip().lower()
    if confirm == 'yes':
        print("Thank you for your order!")
    else:
        print("Order canceled.")
        orders.clear()
