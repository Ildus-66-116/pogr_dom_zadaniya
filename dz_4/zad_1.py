# Напишите функцию для транспонирования матрицы transposed_matrix, принимает в аргументы matrix,
# и возвращает транспонированную матрицу.


def transpose(matrix):
    transpose_matrix = []
    rows = len(matrix)
    cols = len(matrix[0])
    for j in range(cols):
        transposed_row = []
        for i in range(rows):
            transposed_row.append(matrix[i][j])
        transpose_matrix.append(transposed_row)
    return transpose_matrix


print(transpose(matrix=[[1, 2, 3], [4, 5, 6]]))
