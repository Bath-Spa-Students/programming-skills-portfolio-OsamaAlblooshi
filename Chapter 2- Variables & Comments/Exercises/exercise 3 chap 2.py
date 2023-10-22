## Exercise 3: Stripping Names :ballot_box_with_check:

# Initialize a variable with a name containing leading and trailing whitespace
name = "\t\n  Osama \t\n"

# Print the name with whitespace
print("Name with Whitespace:")
print(name)

# Print the name after stripping leading and trailing whitespace
print("Name after Lstrip():")
print(name.lstrip())

print("Name after Rstrip():")
print(name.rstrip())

print("Name after Strip():")
print(name.strip())
