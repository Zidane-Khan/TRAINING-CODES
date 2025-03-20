# Given a squarematrixof sizeN, turn it by 90 degrees in an anti-clockwise direction, as shown in sample input.
#  Input
# Input Format
#  First line will contain the number of rows N (same as the number of columns)
#  After that next N lines will N rows of the matrix.
#  Constraints
#  1 <= N <=1000
#  1 <= Elements Of the Matrix <= 10000
#  Output
# You have to display the rotated matrix.
#  Sample Input 1 
#  4
# 1 2 3 4
# 5 6 7 8
# 1 2 3 4
# 5 6 7 8
# Sample Output 1
# 4 8 4 8
# 3 7 3 7
# 2 6 2 6
# 1 5 1 5

N = int(input())  # Size of the matrix (N x N)
matrix = []

# Reading the matrix
for _ in range(N):
    row = list(map(int, input().split()))  # Read each row and convert to integers
    matrix.append(row)

# Step 2: Rotate the matrix 90 degrees anti-clockwise
rotated_matrix = []

# Create the rotated matrix by taking columns of the original matrix as rows
for j in range(N):
    rotated_row = []
    for i in range(N-1, -1, -1):  # Start from the last row to the first row
        rotated_row.append(matrix[i][j])
    rotated_matrix.append(rotated_row)

# Step 3: Print the rotated matrix
for row in rotated_matrix:
    print(" ".join(map(str, row)))
