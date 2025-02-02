def matrix_multiply(A, B):
    # Check if multiplication is possible
    if len(A[0]) != len(B):
        raise ValueError("Incompatible matrices for multiplication.")
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    # Perform the multiplication
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

# Example matrices
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

# Perform matrix multiplication
result = matrix_multiply(A, B)

# Print the result
for row in result:
    print(row)
