import numpy as np

# Created a 3x3 matrix A
A = np.array([[1, 2, 3], [4, 5, 6], [7, 0, 1]])

index = []
for i in range(3):
    for j in range(3):
        if A[i,j] == 0:
           index.append((i,j))

for ind in index:
    A[ind[0],:] = np.zeros((3,))
    A[:,ind[1]] = np.zeros((3,))


# Print the matrix
print(A)

