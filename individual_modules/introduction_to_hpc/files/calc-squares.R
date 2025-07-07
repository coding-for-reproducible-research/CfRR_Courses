# Initialise a vector with numbers 1 to 1000
numbers <- 1:1000

# Print the initial vector
cat("Initial list of numbers:\n")
print(numbers)

# Calculate the square of each number in the vector
squares <- numeric(length(numbers))
for (i in 1:length(numbers)) {
  squares[i] <- numbers[i]^2
}

# Print the results in full
cat("\nSquares of the numbers:\n")
print(squares)
