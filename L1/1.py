import math


def interpol(x, lstx, lsty, debug=False):
    Pnp1 = math.prod([(x - lstx[i]) for i in range(len(lstx))])
    di = [[(lstx[i] if i != j else x) - lstx[j] for j in range(len(lstx))] for i in
          range(len(lstx))]
    Di = [math.prod(di[i]) for i in range(len(lstx))]
    yiDi = [(lsty[i] / Di[i]).__round__(1) for i in range(len(lstx))]
    syiDi = sum(yiDi)
    res = syiDi * Pnp1
    return res


if __name__ == '__main__':
    x = 0.1157
    lstx = [0.101, 0.106, 0.111, 0.116, 0.121, 0.126]
    lsty = [1.26183, 1.27644, 1.29122, 1.30617, 1.32130, 1.32660]
    ans = interpol(x, lstx, lsty)
    print(ans)
