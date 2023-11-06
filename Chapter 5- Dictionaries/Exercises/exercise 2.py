# Define a Python glossary
glossary = {
    "variable": "A container that holds data or information in a program.",
    "function": "A reusable block of code that performs a specific task.",
    "loop": "A control structure that repeats a block of code multiple times.",
    "list": "An ordered collection of items that can be of any data type.",
    "string": "A sequence of characters, such as text, enclosed in quotes."
}

# Print each word and its meaning with a newline between each pair
for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")
