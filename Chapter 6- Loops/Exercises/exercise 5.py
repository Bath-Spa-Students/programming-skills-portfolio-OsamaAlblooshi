# Create a list of sandwich orders with 'pastrami' appearing at least three times
sandwich_orders = ['tuna', 'turkey', 'pastrami', 'roast beef', 'pastrami', 'veggie', 'pastrami', 'ham and cheese', 'pastrami']

# Create an empty list for finished sandwiches
finished_sandwiches = []

# Check if there is 'pastrami' and remove it
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

if not sandwich_orders:
    print("Sorry, we're out of pastrami.")
else:
    # Process the remaining sandwich orders
    while sandwich_orders:
        current_order = sandwich_orders.pop(0)
        print(f"I made your {current_order} sandwich.")
        finished_sandwiches.append(current_order)

# Print the list of finished sandwiches
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
