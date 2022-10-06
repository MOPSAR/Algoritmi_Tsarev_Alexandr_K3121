def Transporation(matrix, m, n):
    matr_trans = [[0 for i in range(m)] for j in range(n)]
    for i in range(m):
        for j in range(n):
            matr_trans[j][i] = matrix[i][j]
    return matr_trans


def Obr_matrix(matrix):
    alg_dop = [[0 for i in range(3)] for j in range(3)]
    minor2 = []
    for i in range(3):
        for j in range(3):
            minor = []
            for p in range(3):
                for q in range(3):
                    if i != p and j != q: minor.append(matrix[p][q])
            alg_dop[i][j] = (minor[0] * minor[3] - minor[1] * minor[2]) * (-1) ** (i + j)
            minor2.append(minor[0] * minor[3] - minor[1] * minor[2])
    souz_matrix = Transporation(alg_dop, 3, 3)
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


matrix = []
inp = " "
print("Введите матрицу, для окончания ввода нажмите Enter на пустой строке: ")
while inp != "":
    inp = input()
    if inp != "": matrix.append(list(map(int, inp.split())))
print("Обратная матрица: ")
for i in range(3): print(*Obr_matrix(matrix)[i])
