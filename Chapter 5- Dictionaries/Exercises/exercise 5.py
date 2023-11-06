# Create a list of dictionaries representing different pets
pets = [
    {'kind': 'dog', 'owner': 'Alice'},
    {'kind': 'cat', 'owner': 'Bob'},
    {'kind': 'parrot', 'owner': 'Charlie'}
]

# Loop through the list and print information about each pet
for pet in pets:
    kind = pet['kind']
    owner = pet['owner']
    print(f"This is {owner}'s {kind}.")
