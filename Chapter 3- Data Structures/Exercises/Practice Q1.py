#Given a Python list, write a program to remove all occurrences of item 20. 
#Given list: list1 = [5, 20, 15, 20, 25, 50, 20]
# Given list
list1 = [5, 20, 15, 20, 25, 50, 20]

# Remove all occurrences of item 20
list_without_20 = [item for item in list1 if item != 20]

# Print the updated list
print("Original list:", list1)
print("List after removing all occurrences of 20:", list_without_20)
