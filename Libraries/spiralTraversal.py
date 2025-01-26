''' Problem statment:
    Given MATRIX:     1 2 3
                      4 5 6
                      7 8 9 

    Output: 1 2 3 6 9 8 7 4 5 '''

import numpy as np

# Define the matrix
A = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]

output = []

# Define the boundaries of the matrix
top, bottom, left, right = 0, len(A)-1, 0, len(A[0])-1

# While there is still a layer to process
while top <= bottom and left <= right:
    # Traverse the top row (left to right)
    for j in range(left, right + 1):
        output.append(A[top][j])
    top += 1

    # Traverse the right column (top to bottom)
    for i in range(top, bottom + 1):
        output.append(A[i][right])
    right -= 1

    if top <= bottom:
        # Traverse the bottom row (right to left)
        for j in range(right, left - 1, -1):
            output.append(A[bottom][j])
        bottom -= 1

    if left <= right:
        # Traverse the left column (bottom to top)
        for i in range(bottom, top - 1, -1):
            output.append(A[i][left])
        left += 1

# Print the output
print(f"The spiral order of the matrix is: {output}")
