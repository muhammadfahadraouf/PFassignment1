# Accept a string from the user
input_string = input("Enter a string: ")

# Accept the number of characters to remove
n = int(input("Enter the number of characters to remove: "))

# Remove the first n characters and store the modified string
new_string = input_string[n:]

# Print the modified string
print("Modified string after removing first", n, "characters:", new_string)
 