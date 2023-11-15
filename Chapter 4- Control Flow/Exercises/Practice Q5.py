# Get the month as input from the user (assuming a valid integer input)
month = int(input("Enter the month (1-12): "))

# Using elif statements to determine the season based on the month
if 3 <= month <= 5:
    season = "Spring"
elif 6 <= month <= 8:
    season = "Summer"
elif 9 <= month <= 11:
    season = "Fall"
elif month == 12 or 1 <= month <= 2:
    season = "Winter"
else:
    season = "Invalid month"

# Display the result
print("The season for month", month, "is", season)
