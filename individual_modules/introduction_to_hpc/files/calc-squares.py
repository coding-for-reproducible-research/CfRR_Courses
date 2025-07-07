# Initialise a list with numbers 1 to 1000
numbers = list(range(1, 1001))

# Print the initial list
print("Initial list of numbers:")
print(numbers)

# Calculate the square of each number in the list
squares = []
for num in numbers:
    square = num ** 2
    squares.append(square)

# Print the results in full
print("\nSquares of the numbers:")
print(squares)