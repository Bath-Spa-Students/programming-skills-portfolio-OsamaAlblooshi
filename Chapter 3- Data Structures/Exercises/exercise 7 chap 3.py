# Create a list of places to visit
places_to_visit = ["Paris", "Tokyo", "New York", "Venice", "Sydney"]

# Print the list in its original order
print("Original list:")
print(places_to_visit)

# Print the list in alphabetical order using sorted()
print("\nList in alphabetical order (sorted()):")
print(sorted(places_to_visit))

# Verify that the original list is still in its original order
print("\nOriginal list (still in the original order):")
print(places_to_visit)

# Print the list in reverse alphabetical order using sorted() with the reverse=True argument
print("\nList in reverse alphabetical order (sorted() with reverse=True):")
print(sorted(places_to_visit, reverse=True))

# Verify that the original list is still in its original order
print("\nOriginal list (still in the original order):")
print(places_to_visit)

# Change the order of the list using reverse()
places_to_visit.reverse()
print("\nList after using reverse():")
print(places_to_visit)

# Change the order of the list using reverse() again to return to the original order
places_to_visit.reverse()
print("\nList after using reverse() to restore the original order:")
print(places_to_visit)

# Change the order of the list to alphabetical order using sort()
places_to_visit.sort()
print("\nList in alphabetical order (sorted using sort()):")
print(places_to_visit)

# Change the order of the list to reverse alphabetical order using sort() with the reverse=True argument
places_to_visit.sort(reverse=True)
print("\nList in reverse alphabetical order (sorted using sort() with reverse=True):")
print(places_to_visit)
