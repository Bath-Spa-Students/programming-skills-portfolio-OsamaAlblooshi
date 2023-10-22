# Create a list of people to invite to dinner
guest_list = ["Albert Einstein", "Leonardo da Vinci", "Marie Curie"]

# Print initial invitation messages
for person in guest_list:
    print(f"Dear {person},\nYou are cordially invited to dinner at my place. Please join us for a delightful evening of conversation and good food!\nSincerely, [Your Name]\n")

# Simulate a guest who can't make it
guest_cant_make_it = "Albert Einstein"
print(f"{guest_cant_make_it} can't make it to the dinner.\n")

# Replace the guest who can't make it with a new person
new_guest = "Osama"
guest_list.remove(guest_cant_make_it)
guest_list.append(new_guest)

# Print a second set of invitation messages
for person in guest_list:
    print(f"Dear {person},\nYou are cordially invited to dinner at my place. Please join us for a delightful evening of conversation and good food!\nSincerely, [Your Name]\n")
