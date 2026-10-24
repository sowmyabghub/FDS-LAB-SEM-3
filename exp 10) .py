
# Experiment No: 10
# Experiment to Understand Array Functions in Data Science
# Using NumPy Library

import numpy as np

# Create a random array of 9 integers between 1 and 99
array = np.random.randint(1, 100, 9)
print("Original Array:")
print(array)

# Square root of array elements
print("\nSquare Root of Array:")
print(np.sqrt(array))

# Find the number of dimensions
print("\nNumber of Dimensions:")
print(array.ndim)

# Reshape 1D array into 3x3 matrix
new_array = array.reshape(3, 3)
print("\nReshaped 3x3 Array:")
print(new_array)

# Find dimensions of the new array
print("\nDimensions of New Array:")
print(new_array.ndim)

# Convert 2D array into 1D array
print("\nRavel Array:")
print(new_array.ravel())

# Reshape array into 3x3 matrix again
newm = new_array.reshape(3, 3)
print("\nNew Matrix:")
print(newm)

# Access elements in the third row, columns 2 and 3
print("\nElements newm[2, 1:3]:")
print(newm[2, 1:3])

# Access elements in the second row, columns 2 and 3
print("\nElements newm[1:2, 1:3]:")
print(newm[1:2, 1:3])

# Select all rows and no columns
print("\nElements new_array[0:3, 0:0]:")
print(new_array[0:3, 0:0])

# Select first two rows and first column
print("\nElements new_array[0:2, 0:1]:")
print(new_array[0:2, 0:1])

# Select all rows and first column
print("\nElements new_array[0:3, 0:1]:")
print(new_array[0:3, 0:1])

# Select second and third rows
print("\nElements new_array[1:3]:")
print(new_array[1:3])