# Dictionary of major rivers and the countries they run through
rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China'
}

# 1. Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

# 2. Print the name of each river
print("\nRivers:")
for river in rivers.keys():
    print(river)

# 3. Print the name of each country
print("\nCountries:")
for country in rivers.values():
    print(country)
