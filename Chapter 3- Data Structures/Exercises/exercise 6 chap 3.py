# Create a list of people to invite to dinner
guest_list = ["Albert Einstein", "Leonardo da Vinci", "Marie Curie", "Osama"]

# Print initial invitation messages
for person in guest_list:
    print(f"Dear {person},\nYou are cordially invited to dinner at my place. Please join us for a delightful evening of conversation and good food!\nSincerely, [Your Name]\n")

# Print a message that you can invite only two people
print("I can only invite two people for dinner.\n")

# Use pop() to remove guests until only two names remain
while len(guest_list) > 2:
    removed_person = guest_list.pop()
    print(f"Sorry, {removed_person}, I can't invite you to dinner this time.\n")

# Print a message to the two people still on your list
for person in guest_list:
    print(f"Dear {person},\nYou are still invited to dinner at my place. Please join us for a delightful evening of conversation and good food!\n")

# Use del to remove the last two names from your list
del guest_list[0]
del guest_list[0]

# Print your list to confirm it's empty
print("Guest list is now empty:", guest_list)
