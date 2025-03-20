n = int(input())  # Size of the matrix
matrix = []

# Input the matrix
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

total_sum = 0

# Loop over the matrix to sum the boundary elements
for i in range(n):
    for j in range(n):
        # Check if it's a boundary element
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            total_sum += matrix[i][j]
        # Check if it's a diagonal element (not already counted)
        elif i == j or i + j == n - 1:
            total_sum += matrix[i][j]

# Output the result
print(total_sum)