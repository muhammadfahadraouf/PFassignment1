# Accept a string from the user
user_input = input("Enter a string: ")

# Initialize an empty string to store characters at even index numbers
even_index_chars = ''

# Iterate through the characters in the input string
for index, char in enumerate(user_input):
    # Check if the index is even
    if index % 2 == 0:
        # Append the character at the even index to the result string
        even_index_chars += char

# Print the characters at even index numbers
print("Characters at even index numbers:", even_index_chars)
