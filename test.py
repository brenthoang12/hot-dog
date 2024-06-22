import numpy as np
import os

# Create a 2D array with shape (3, 4)
x = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

print("Original shape:", x.shape)
print("Original array:\n", x)


# Reshape the array to add a new dimension at the beginning
x = x.reshape((1,) + x.shape)

print("New shape:", x.shape)
print("Reshaped array:\n", x)

import subprocess
 
# Using system() method to
# execute shell commands
subprocess.Popen('echo "Geeks 4 Geeks"', shell=True)