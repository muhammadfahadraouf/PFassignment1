# Accept an integer from the user
num = int(input("Enter an integer: "))

# Initialize an empty string to store the reversed digits
reversed_digits = ''

# Convert the integer to a string and reverse it
num_str = str(num)
reversed_str = num_str[::-1]

# Iterate over each character (digit) in the reversed string
for digit in reversed_str:
    # Add each digit to the reversed_digits string with a space
    reversed_digits += digit + ' '

# Print the reversed digits with spaces in between
print("Reversed digits:", reversed_digits.strip())

