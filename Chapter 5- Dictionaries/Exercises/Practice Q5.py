# Two dictionaries to be merged
dict1 = {"name": "John", "age": 25, "city": "New York"}
dict2 = {"occupation": "Engineer", "hobbies": ["Reading", "Coding"]}

# Merging dictionaries using {**d1, **d2}
merged_dict = {**dict1, **dict2}

# Printing the merged dictionary
print("Merged Dictionary:")
print(merged_dict)
