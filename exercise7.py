# Define the number of rows for the pattern
num_rows = 5

# Iterate through the rows
for i in range(1, num_rows + 1):
    # Print each number repeating based on the row number
    for j in range(i):
        print(i, end=' ')  # Use end=' ' to print in the same line with space
    print()  # Move to the next line after printing each row
