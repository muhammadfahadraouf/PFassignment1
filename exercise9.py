# Given two lists
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

# Create a new list using list comprehension
new_list = [num for num in list1 if num % 2 != 0] + [num for num in list2 if num % 2 == 0]

# Print the new list
print("New list:", new_list)

