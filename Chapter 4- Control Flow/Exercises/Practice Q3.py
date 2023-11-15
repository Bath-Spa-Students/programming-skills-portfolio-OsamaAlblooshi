
# Assuming you have variables named 'amount1' and 'amount2'
amount1 = 15  # You can change the value of amount1 as needed
amount2 = 80  # You can change the value of amount2 as needed

# Nested decision structures
if amount1 > 10:
    if amount2 < 100:
        # Display the greater of amount1 and amount2
        if amount1 > amount2:
            print("The greater amount is:", amount1)
        else:
            print("The greater amount is:", amount2)
    else:
        print("amount2 is not less than 100.")
else:
    print("amount1 is not greater than 10.")
