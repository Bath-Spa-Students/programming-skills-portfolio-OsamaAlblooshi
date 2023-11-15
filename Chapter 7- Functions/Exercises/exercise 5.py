def describe_city(city, country="Default Country"):
    """Prints a sentence describing the city and its country."""
    print(f"{city} is in {country}.")

# Call the function for three different cities
describe_city("Reykjavik", "Iceland")
describe_city("New York", "USA")
describe_city("Tokyo")  # This will use the default country value
