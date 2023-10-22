## Exercise 5: USB Shopper :ballot_box_with_check:
# Define the girl's budget and the price of one USB stick
budget = 50
usb_price = 6

# Calculate how many USB sticks she can buy
usb_quantity = budget // usb_price

# Calculate the pounds left after buying USB sticks
pounds_left = budget % usb_price

# Display the results
print("She can buy", usb_quantity, "USB sticks.")
print("She will have £", pounds_left, "left.")
