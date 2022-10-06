import timeit
import numpy as np


def Obr_matrix(matrix):
    obr_matrix=np.array(matrix)
    return np.linalg.inv(obr_matrix)


print(timeit.timeit(stmt="Obr_matrix([[1,2,3],[8,9,5],[6,7,4]])",setup="from __main__ import Obr_matrix",number=100000)/100000)

