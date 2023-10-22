# Create a list of friends' names
names = ["Osama", "Ahmed", "Khalid", "Ali", "Saleem"]

# Print a personalized message to each person
message = "Hello, {}! I hope you're having a great day."

for name in names:
    personalized_message = message.format(name)
    print(personalized_message)
