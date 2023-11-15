#Write a Python program to iterate through the keys of a dictionary and print them.
# Creating a dictionary
myself_info = {
    "name": "Osama ALblooshi",
    "age": 24,
    "location": "Ras Al Khaimah, UAE",
    "occupation": "Customer Service Representative",
    "hobbies": ["Reading"],
    "email": "osamaibrahim053@gmail.com"
}

# Iterating through the keys and printing them
print("Keys in the dictionary:")
for key in myself_info.keys():
    print(key)
