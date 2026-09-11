import random

# Review: Variables & Random Number Genertions
item_name = "Gaming Mouse"
price = 49.99
stock = random.randint(3, 8)    # Generates 3 to 8 items in stock

# Display item information
print("--- WELCOME TO THE SHOP ---")
print(f"item: {item_name} | Price: ${price}")

# Checkout system loop
while stock > 0:
    print(f"\nAvailable stock: {stock} units\n")

    # Get user input
    user_input = input("How many do you want to buy? (or type 'exit'): ")

    # Check for exit command
    if user_input.lower() == "exit":
        print("Thank you for visiting! Goodbye.")
        break

    # Convert input string to integer
    quantity = int(user_input) 

    # Process order if enough stock is available
    if quantity <= stock:
        total_cost = quantity * price
        stock = stock - quantity    # Update stock

        print(f"Success! You bought {quantity}x {item_name}.")
        print(f"Total price: ${total_cost:.2f}")
    else:
        print(f"Error: Not enough in stock! Only {stock} left.")    

# Triggered when stock reaches zero
if stock == 0:
    print("\n[SOLD OUT] We are completely out of stock!")
