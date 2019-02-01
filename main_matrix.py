from playLA.Matrix import Matrix

if __name__ == '__main__':

    matrix = Matrix([[1, 2], [3, 4]])
    print(matrix)
    print("matrix.shape = {}".format(matrix.shape()))
    print("matrix.size = {}".format(matrix.size()))
    print("len(matrix) = {}".format(len(matrix)))
    print("matrix[0][0] = {}".format(matrix[0, 0]))
    print("The {} row_vector is {}".format(1, matrix.row_vector(1)))
    print("The {} col_vector is {}".format(1, matrix.col_vector(1)))

    matrix2 = Matrix([[5, 6], [7, 8]])
    print("add: {}".format(matrix + matrix2))
    print("substract: {}".format(matrix - matrix2))

    print("scalar-mul: {}".format(matrix * 2))
    print("scalar-rmul: {}".format(2 * matrix))
    print("zero_2_3: {}".format(Matrix.zero(2, 3)))