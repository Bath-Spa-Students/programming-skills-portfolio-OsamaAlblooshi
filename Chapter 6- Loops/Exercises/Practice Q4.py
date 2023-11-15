# Using the break statement to exit a for loop when a specific condition is met
for number in range(1, 11):
    if number == 5:
        print("Breaking the loop at", number)
        break
    print(number)
