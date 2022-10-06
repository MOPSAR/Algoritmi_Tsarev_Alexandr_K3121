import timeit
def Transporation(matrix, m, n):
    matr_trans = [[0 for i in range(m)] for j in range(n)]
    for i in range(m):
        for j in range(n):
            matr_trans[j][i] = matrix[i][j]
    return matr_trans


def Obr_matrix(matrix):
    souz_martix = [[0 for i in range(3)] for j in range(3)]
    minor2 = []
    for i in range(3):
        for j in range(3):
            minor = []
            for p in range(3):
                for q in range(3):
                    if i != p and j != q: minor.append(matrix[p][q])
            souz_martix[i][j] = (minor[0] * minor[3] - minor[1] * minor[2]) * (-1) ** (i + j)
            minor2.append(minor[0] * minor[3] - minor[1] * minor[2])
    obr_matrix = Transporation(souz_martix, 3, 3)
    det = matrix[0][0] * minor2[0] - matrix[0][1] * minor2[1] + matrix[0][2] * minor2[2]
    if det == 0:
        print("Обратную матрицу невозможно найти, так как детерминант матрицы равен нулю!!!! ")
        for i in range(3):
            for j in range(3):
                obr_matrix[i][j] = 0
        return obr_matrix
    else:
        for i in range(3):
            for j in range(3):
                obr_matrix[i][j] *= 1 / det
        return obr_matrix
print(timeit.timeit(stmt="Obr_matrix([[1,2,3],[8,9,5],[6,7,4]])",setup="from __main__ import Obr_matrix",number=100000)/100000)

