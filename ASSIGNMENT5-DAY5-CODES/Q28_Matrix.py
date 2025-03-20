# # 28. Write a Python class Matrix that represents a matrix and has methods for 
# # matrix addition and multiplication.

class Matrix:
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2

    def add_matrix(self):
        add_mat = []
        for i in range(len(self.matrix1)):
            row = []
            for j in range(len(self.matrix2[i])):
                row.append(self.matrix1[i][j] + self.matrix2[i][j])
            add_mat.append(row)
        return add_mat

    def sub_matrix(self):
        sub_mat = []
        for i in range(len(self.matrix1)):
            row = []
            for j in range(len(self.matrix2[i])):
                row.append(self.matrix1[i][j] - self.matrix2[i][j])  # Fix subtraction
            sub_mat.append(row)
        return sub_mat

# Creating the Matrix object
obj1 = Matrix(
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
)

# Calling the methods
added_matrix = obj1.add_matrix()  # Returns the sum of the matrices
subtracted_matrix = obj1.sub_matrix()  # Returns the difference of the matrices

print("Added Matrix:")
for row in added_matrix:
    print(row)

# print("\nSubtracted Matrix:")
# for row in subtracted_matrix:
#     print(row)


# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# matrix2 = [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ]

# add_mat=[]

# for i in range(len(matrix1)):
#     row=[]
#     for j in range(len(matrix2[i])):

        
#         row.append(matrix1[i][j]+matrix2[i][j])
#     add_mat.append(row)
# print(add_mat)



# sub_mat=[]

# for i in range(len(matrix1)):
#     row=[]
#     for j in range(len(matrix2[i])):

        
#         row.append(matrix1[i][j]-matrix2[i][j])
#     sub_mat.append(row)
# print(sub_mat)
    # print("enter i first element: ")
    # for j in range(len(matrix2)):
    #     add_mat=matrix1[i]+ matrix2[j]

    #     print(add_mat)

