import numpy as np


def Transporation(matrix):
    matr_trans = np.array(matrix)
    return matr_trans.transpose()


def Proizvedenie(matrix, matrix1):
    mat1 = np.array(matrix)
    mat2 = np.array(matrix1)
    return np.dot(mat1, mat2)


def Rang(matrix):
    mat = np.array(matrix)
    return np.linalg.matrix_rank(mat)


matrix = []
inp = " "
print("Введите матрицу, для окончания ввода нажмите Enter на пустой строке: ")
while inp != "":
    inp = input()
    if inp != "": matrix.append(list(map(int, inp.split())))
operation = input("Введите операцию, которую хотите совершить: T-транспорация матрицы, *-умножение, R-ранг: ")
if operation == "T":
    print("Транспонированная матрица:")
    trans_matrix=Transporation(matrix)
    for i in range(len(matrix[0])): print(*trans_matrix[i])
if operation == "*":
    print("Введите 2-ую матрицу: ")
    matrix1 = []
    inp = " "
    while inp != "":
        inp = input()
        if inp != "": matrix1.append(list(map(int, inp.split())))
    print("Произведение матриц:")
    proizv_matrix=Proizvedenie(matrix, matrix1)
    for i in range(len(matrix)): print(*proizv_matrix[i])
if operation=="R": print("Ранг матрицы: "+str(Rang(matrix)))
