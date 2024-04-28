import numpy as np

m = 1
n = 4

a = np.array([[5, 7, 6, 5],
              [7, 10, 8, 7],
              [6, 8, 10, 9],
              [5, 7, 9, 10]])
b = np.array([23, 32, 33, 31])

d = np.eye(4)
s = np.zeros((4, 4))

for i in range(n):
    d[i][i] = np.sign(a[i][i] - sum([s[p][i] * s[p][i] * d[p][p] for p in range(i)]))
    s[i][i] = np.sqrt(np.abs(a[i][i] - sum([s[p][i] * s[p][i] * d[p][p] for p in range(i)])))
    for j in range(i, n):
        s[i][j] = (a[i][j] - sum([s[p][i] * s[p][j] * d[p][p] for p in range(i)])) / (
                    d[i][i] * s[i][i])

st = s.transpose().dot(d)

ans_y = [1] * n
for k in range(n):
    ans_y[k] = (b[k] - sum([st[k][j] * ans_y[j] for j in range(k)])) / st[k][k]

ans = [1] * n
for k in range(n - 1, -1, -1):
    ans[k] = (ans_y[k] - sum([s[k][j] * ans[j] for j in range(k + 1, n)])) / s[k][k]

print('Исходные данные:')
for i in range(len(a)):
    for j in a[i]:
        print(str(j).ljust(3), end=' ')
    print(b[i])


print('Решение: ')
for i in ans:
    print(round(i, 5))
