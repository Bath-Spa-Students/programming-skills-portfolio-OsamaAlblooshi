# Using a while loop to find the largest number among user-input values
largest_number = float('-inf')  # Initialize with negative infinity

while True:
    user_input = float(input("Enter a number (enter '0' to exit): "))
    
    if user_input == 0:
        break
    
    if user_input > largest_number:
        largest_number = user_input

print("The largest number entered is:", largest_number)
