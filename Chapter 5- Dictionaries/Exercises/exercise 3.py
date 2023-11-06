# Define a Python glossary
glossary = {
    "variable": "A container that holds data or information in a program.",
    "function": "A reusable block of code that performs a specific task.",
    "loop": "A control structure that repeats a block of code multiple times.",
    "list": "An ordered collection of items that can be of any data type.",
    "string": "A sequence of characters, such as text, enclosed in quotes.",
    "dictionary": "A collection of key-value pairs.",
    "tuple": "An ordered, immutable collection of items.",
    "module": "A file containing Python code that can be reused in other programs.",
    "boolean": "A data type that represents either True or False.",
    "iteration": "The process of repeatedly executing a block of code."
}

# Print the glossary using a loop
for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")
