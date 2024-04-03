# Initialize the previous number as 0
prev_num = 0

# Iterate through the first 10 numbers
for current_num in range(1, 11):
    # Calculate the sum of the current and previous numbers
    sum_numbers = current_num + prev_num
    
    # Print the sum
    print("Sum of", current_num, "and", prev_num, "is:", sum_numbers)
    
    # Update the previous number for the next iteration
    prev_num = current_num
