def Transporation(matrix, m, n):
    matr_trans = [[0 for i in range(m)] for j in range(n)]
    for i in range(m):
        for j in range(n):
            matr_trans[j][i] = matrix[i][j]
    return matr_trans


def Proizvedenie(matrix, matrix1, m, p, n):
    matr_proizv = [[0 for i in range(p)] for j in range(m)]
    for i in range(m):
        for j in range(p):
            for e in range(n):
                matr_proizv[i][j] += matrix[i][e] * matrix1[e][j]
    return matr_proizv


def Rang(matrix):
    minor2 = []
    rang = 0
    t = 0
    for i in range(3):
        for j in range(3):
            minor = []
            for p in range(3):
                for q in range(3):
                    if i != p and j != q:
                        if minor != 0 and t == 0:
                            rang = 1
                            t = 1
                        minor.append(matrix[p][q])
            minorr2 = minor[0] * minor[3] - minor[1] * minor[2]
            if minorr2 != 0: rang = 2
            minor2.append(minorr2)
    minor3= matrix[0][0] * minor2[0] - matrix[0][1] * minor2[1] + matrix[0][2] * minor2[2]
    if minor3!= 0: rang=3
    return rang


matrix = []
inp = " "
print("Введите строки матрицы(каждую с новой строки; элементы матрицы через пробел), для окончания ввода нажмите Enter на пустой строке: ")
while inp != "":
    inp = input()
    if inp != "": matrix.append(list(map(int, inp.split())))
m = len(matrix)
n = len(matrix[0])
operation = input(
    "Введите операцию, которую хотите совершить: T-транспонирование матрицы, *-умножение, R-ранг(работает только для матриц размерности 3 на 3): ")
if operation == "T":
    print("Транспонированная матрица:")
    trans_matrix = Transporation(matrix, m, n)
    for i in range(n): print(*trans_matrix[i])
if operation == "*":
    print("Введите 2-ую матрицу: ")
    matrix1 = []
    inp = " "
    while inp != "":
        inp = input()
        if inp != "": matrix1.append(list(map(int, inp.split())))
    q = len(matrix1)
    p = len(matrix1[0])
    if q==n:
        print("Произведение матриц:")
        proizv_matrix = Proizvedenie(matrix, matrix1, m, p, n)
    else: print("Матрицы не согласованы!!!!")
    for i in range(m): print(*proizv_matrix[i])
if operation=="R": print("Ранг матрицы: "+str(Rang(matrix)))


