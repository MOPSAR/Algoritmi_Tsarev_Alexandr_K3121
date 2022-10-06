import numpy as np

def Obr_matrix(matrix):
    obr_matrix=np.array(matrix)
    return np.linalg.inv(obr_matrix)


matrix = []
inp = " "
print("Введите матрицу, для окончания ввода нажмите Enter на пустой строке: ")
while inp != "":
    inp = input()
    if inp!="": matrix.append(list(map(int, inp.split())))
print("Обратная матрица: ")
obr_matrix=Obr_matrix(matrix)
for i in range(3): print(*obr_matrix[i])
