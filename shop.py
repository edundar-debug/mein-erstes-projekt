import random

# Review: Variables & Random Number Genertions
item_name = "Gaming Mouse"
price = 49.99
stock = random.randint(1, 5)

# Display item information
print("--- WELCOME TO THE SHOP ---")
print(f"item: {item_name}")
print(f"Price: ${price}")
print(f"Available stock: {stock}units/n")

# New Concept: Conditionals (if / else)
order_quantity = 3 

if order_quantity <= stock:
    total_cost = order_quantity * price
    print(f"Succes! You bought {order_quantity}x {item_name}.")
    print(f"Total price: ${total_cost:.2f}")
else:
    print(f"Error: Not enough in stock! Only {stock} units left.")
