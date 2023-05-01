#Transpose of the matrix
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Ask user to input the elements of the matrix
matrix = []
print("Enter the elements of the matrix row-wise:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input())
        row.append(element)
    matrix.append(row)

# Find the transpose matrix
transpose_matrix = []
for j in range(cols):
    row = []
    for i in range(rows):
        element = matrix[i][j]
        row.append(element)
    transpose_matrix.append(row)

print("The input matrix:")
for row in matrix:
    print(row)

# Print the transpose matrix
print("Transpose of the matrix:")
for row in transpose_matrix:
    print(row)
