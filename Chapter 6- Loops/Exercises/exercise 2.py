while True:
    age_str = input("Please enter your age (or 'quit' to exit): ")

    if age_str.lower() == 'quit':
        break

    try:
        age = int(age_str)
        if age < 3:
            ticket_price = 0
        elif 3 <= age <= 12:
            ticket_price = 10
        else:
            ticket_price = 15

        print(f"The cost of your movie ticket is ${ticket_price}")
    except ValueError:
        print("Please enter a valid age or 'quit' to exit.")
