def interpol(x, lsty, lstx):
    n = len(lsty)
    m = len(lstx)
    s = 0
    for i in range(0, n):
        p = lsty[i]
        for j in range(0, m):
            if i != j:
                p = p * (x - lstx[j])/(lstx[i] - lstx[j])
        s = s + p
    res = s
    return res


if __name__ == '__main__':
    start_y = [0, 0.5, 1]
    start_x = [0, 1/6, 0.5]
    ans = interpol(1/4, start_y, start_x)
    print('Результат при x=1/4:', round(ans, 5))
    ans = interpol(1/3, start_y, start_x)
    print('Результат при x=1/3:', round(ans, 5))

