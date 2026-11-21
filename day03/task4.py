matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


print("Original Matrix:")
print(matrix)

transpose = [[matrix[row][col] for row in range(3)] for col in range(3)]
print("Transpose Matrix:")
print(transpose)