# Create a list of sandwich orders
sandwich_orders = ['tuna', 'turkey', 'pastrami', 'roast beef', 'pastrami', 'veggie', 'pastrami', 'ham and cheese']

# Create an empty list for finished sandwiches
finished_sandwiches = []

# Process sandwich orders
while sandwich_orders:
    current_order = sandwich_orders.pop(0)

    if current_order == 'pastrami':
        print(f"Sorry, we're out of pastrami.")
    else:
        print(f"I made your {current_order} sandwich.")
        finished_sandwiches.append(current_order)

# Print the list of finished sandwiches
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
