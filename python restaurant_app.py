# Advanced Restaurant App (Terminal Version)

menu = {
    "Veg": {
        "Starters": {
            "Gobi Manchuria": 178.50,
            "Paneer Manchuria": 178.50,
            "Mushroom Manchuria": 178.50,
            "Paneer 65": 178.50
        },
        "Main Course": {
            "Paneer Butter Masala": 168.00,
            "Kadai Paneer": 178.50,
            "Palak Paneer": 168.00
        },
        "Rotis": {
            "Butter Naan": 27.00,
            "Tandoori Roti": 15.75
        },
        "Drinks": {
            "Cool Drink": 30.00
        }
    },
    "Non-Veg": {
        "Starters": {
            "Chicken 65": 147.00,
            "Chilly Chicken": 147.00
        },
        "Main Course": {
            "Chicken Curry": 210.00,
            "Butter Chicken": 210.00
        },
        "Biryani": {
            "Chicken Biryani": 210.00,
            "Mutton Biryani": 273.00
        },
        "Rotis": {
            "Butter Naan": 27.00,
            "Tandoori Roti": 15.75
        },
        "Drinks": {
            "Cool Drink": 30.00
        }
    }
}

cart = {}

def show_main():
    print("\n====== RESTAURANT ======")
    print("1. Veg")
    print("2. Non-Veg")
    print("3. View Cart")
    print("4. Exit")

def show_categories(food_type):
    while True:
        categories = list(menu[food_type].keys())
        print(f"\n--- {food_type} Categories ---")
        
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")
        print(f"{len(categories)+1}. Back")

        choice = input("Choose category: ")

        if not choice.isdigit():
            continue

        choice = int(choice)

        if choice == len(categories) + 1:
            return

        if 1 <= choice <= len(categories):
            show_items(food_type, categories[choice - 1])

def show_items(food_type, category):
    while True:
        items = list(menu[food_type][category].items())
        print(f"\n--- {category} ---")

        for i, (item, price) in enumerate(items, 1):
            print(f"{i}. {item} - ₹{price}")
        print(f"{len(items)+1}. Back")

        choice = input("Choose item: ")

        if not choice.isdigit():
            continue

        choice = int(choice)

        if choice == len(items) + 1:
            return

        if 1 <= choice <= len(items):
            item, price = items[choice - 1]
            qty = input("Enter quantity: ")

            if not qty.isdigit():
                continue

            qty = int(qty)

            if item in cart:
                cart[item]["qty"] += qty
            else:
                cart[item] = {"price": price, "qty": qty}

            print(f"{item} added!")

def show_cart():
    while True:
        print("\n====== CART ======")
        total = 0

        if not cart:
            print("Cart is empty.")
        else:
            items_list = list(cart.items())

            for i, (item, details) in enumerate(items_list, 1):
                item_total = details["price"] * details["qty"]
                total += item_total
                print(f"{i}. {item} x {details['qty']} = ₹{item_total}")

            gst = total * 0.05
            final = total + gst

            print("------------------")
            print(f"Subtotal: ₹{total}")
            print(f"GST (5%): ₹{gst:.2f}")
            print(f"Total: ₹{final:.2f}")
            print("------------------")

        print("\nOptions:")
        print("1. Edit Quantity")
        print("2. Remove Item")
        print("3. Back")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            edit_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            return
        elif choice == "4":
            exit()

def edit_item():
    if not cart:
        print("Cart empty!")
        return

    items_list = list(cart.keys())

    for i, item in enumerate(items_list, 1):
        print(f"{i}. {item}")

    choice = input("Select item to edit: ")

    if not choice.isdigit():
        return

    choice = int(choice)

    if 1 <= choice <= len(items_list):
        item = items_list[choice - 1]
        qty = input("Enter new quantity: ")

        if not qty.isdigit():
            return

        qty = int(qty)

        if qty <= 0:
            del cart[item]
        else:
            cart[item]["qty"] = qty

        print("Quantity updated!")

def remove_item():
    if not cart:
        print("Cart empty!")
        return

    items_list = list(cart.keys())

    for i, item in enumerate(items_list, 1):
        print(f"{i}. {item}")

    choice = input("Select item to remove: ")

    if not choice.isdigit():
        return

    choice = int(choice)

    if 1 <= choice <= len(items_list):
        item = items_list[choice - 1]
        del cart[item]
        print(f"{item} removed!")

# Main loop
while True:
    show_main()
    choice = input("Enter choice: ")

    if choice == "1":
        show_categories("Veg")
    elif choice == "2":
        show_categories("Non-Veg")
    elif choice == "3":
        show_cart()
    elif choice == "4":
        print("Thank you! Visit again 😊")
        break