import numpy as np


def triangle_factorization(matrix, rows, free):
    """Треугольная факторизация"""
    right = np.eye(rows)
    left = np.zeros((rows, rows))

    for i in range(rows):
        left[i][0] = matrix[i][0]
    for j in range(1, rows):
        right[0][j] = matrix[j][0] / left[0][0]

    for i in range(1, rows):

        s = 0
        for j in range(i):
            s += left[i][j] * right[j][i]
        left[i][i] = matrix[i][i] - s

        for t in range(i+1, rows):
            s = 0
            for j in range(i):
                s += left[t][j] * right[j][i]
            left[t][i] = matrix[t][i] - s
            s = 0
            for j in range(i):
                s += left[i][j] * right[j][t]
            right[i][t] = (matrix[i][t] - s)/left[i][i]

    z = np.zeros(4)
    z[0] = free[0]/left[0][0]
    for i in range(1, rows):
        s = 0
        for k in range(i):
            s += left[i][k] * z[k]
        z[i] = (free[i] - s)/left[i][i]

    result = np.zeros(4)
    result[rows-1] = z[rows-1]
    for i in range(rows-2, -1, -1):
        s = 0
        for j in range(i+1, rows):
            s += right[i][j] * result[j]
        result[i] = z[i] - s
    return result


# Контрольный пример
a = np.array([[5, 7, 6, 5],
              [7, 10, 8, 7],
              [6, 8, 10, 9],
              [5, 7, 9, 10]])
b = np.array([23, 32, 33, 31])
n = 4

answer = triangle_factorization(a, n, b)
print('Исходные данные:')
for k in range(n):
    for j in range(n):
        print(f'{a[k][j]} ', end='')
    print('')

print('\nРезультат:')
for j in range(n):
    print(round(answer[j], 5))
