pizza_toppings = []

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ").lower()

    if topping == 'quit':
        break

    print(f"You'll add {topping} to your pizza.")
    pizza_toppings.append(topping)

print("Your pizza will have the following toppings:")
for topping in pizza_toppings:
    print(topping)
