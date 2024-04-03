# Accept a number from the user
num = int(input("Enter a number: "))

# Convert the number to a string to check for palindrome
num_str = str(num)

# Reverse the number using slicing
reversed_num_str = num_str[::-1]

# Check if the original number is equal to its reversed version
if num_str == reversed_num_str:
