```python
# ==========================================
#   CAMPUS CANTEEN BILLING SYSTEM
#   Theme: Black & Pink
# ==========================================

print("\n" + "=" * 45)
print("       CAMPUS CANTEEN BILLING")
print("          BLACK & PINK")
print("=" * 45)

# Menu
print("\n----------- CANTEEN MENU -----------")
print("1. Zinger Burger       - PKR 450")
print("2. Pizza               - PKR 350")
print("3. Fries               - PKR 200")
print("4. Cold Drink          - PKR 100")
print("------------------------------------")
print("Enter 0 to checkout.")

# Prices
burger_price = 450
pizza_price = 350
fries_price = 200
drink_price = 100

# Billing variables
subtotal = 0
total_quantity = 0

# Ordering system
while True:

    print("\n------------------------------------")
    choice = input("Select an item (1-4) or 0 to checkout: ")

    # Checkout
    if choice == "0":
        break

    # Validate item selection
    elif choice not in ["1", "2", "3", "4"]:
        print("Invalid choice! Please select from 1 to 4.")
        continue

    # Ask for quantity
    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Quantity must be greater than zero!")
        continue

    # Calculate item total
    if choice == "1":
        item_name = "Zinger Burger"
        price = burger_price

    elif choice == "2":
        item_name = "Pizza"
        price = pizza_price

    elif choice == "3":
        item_name = "Fries"
        price = fries_price

    else:
        item_name = "Cold Drink"
        price = drink_price

    item_total = price * quantity

    # Update bill
    subtotal = subtotal + item_total
    total_quantity = total_quantity + quantity

    print("\nItem added successfully!")
    print("Item:", item_name)
    print("Price: PKR", price)
    print("Quantity:", quantity)
    print("Item Total: PKR", item_total)

# Apply discount
discount = 0

if subtotal >= 1000:
    discount = subtotal * 0.10

final_bill = subtotal - discount

# Final receipt
print("\n" + "=" * 45)
print("             FINAL RECEIPT")
print("=" * 45)
print("Subtotal:       PKR", format(subtotal, ".2f"))
print("Total Quantity: ", total_quantity)

if discount > 0:
    print("Discount (10%): PKR", format(discount, ".2f"))
else:
    print("Discount:       PKR 0.00")
    print("Spend PKR 1000 or more to get a 10% discount!")

print("-" * 45)
print("FINAL BILL:     PKR", format(final_bill, ".2f"))
print("=" * 45)
print("     Thank you for visiting!")
print("       Visit us again!")
print("=" * 45)
```
