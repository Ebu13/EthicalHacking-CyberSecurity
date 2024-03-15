import time
import numpy as np


def matrix_printer():
    matrix_size = 100
    random_matrix = np.random.rand(matrix_size, matrix_size)
    inverse_matrix = np.linalg.inv(random_matrix)
    for row in inverse_matrix:
        for item in row:
            print(item)


def ortolcum(tekrar):
    surec = 0
    for i in range(tekrar):
        start = time.time()
        matrix_printer()
        end = time.time()
        surec += (end - start)
    return surec / tekrar


print("matrix_printer() fonksiyonunun ortalama calisma suresi ", ortolcum(50))
