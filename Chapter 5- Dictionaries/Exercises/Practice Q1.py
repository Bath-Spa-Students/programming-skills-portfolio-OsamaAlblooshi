#Use a dictionary to store information about yourself.
# Creating a dictionary to store information about yourself
myself_info = {
    "name": "Osama ALblooshi",
    "age": 24,
    "location": "Ras Al Khaimah, UAE",
    "occupation": "Customer Service Representative",
    "hobbies": ["Reading"],
    "email": "osamaibrahim053@gmail.com"
}

# Accessing and printing information from the dictionary
print("Name:", myself_info["name"])
print("Age:", myself_info["age"])
print("Location:", myself_info["location"])
print("Occupation:", myself_info["occupation"])
print("Hobbies:", ', '.join(myself_info["hobbies"]))
print("Email:", myself_info["email"])
