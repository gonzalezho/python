# Create a list of squares from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Create a list of even numbers from 0 to 9
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

# Create a list of tuples (x, y) for x in range(3) and y in range(3)
tuples = [(x, y) for x in range(3) for y in range(3)]
print(tuples)  # Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# Flatten a nested list
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Apply a function to each element in a list
def square(x):
    return x**2

squared_numbers = [square(x) for x in range(10)]
print(squared_numbers)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
