import math
import pandas
def interpol(x, lstx, lsty):
    Pnp1 =  math.prod([(x - lstx[i]) for i in range(len(lstx))])
    di=[[(lstx[i] if i!=j else x)-lstx[j] for j in range(len(lstx))] for i in range(len(lstx))]
    Di=[math.prod(di[i]) for i in range(len(lstx))]
    yiDi = [(lsty[i] / Di[i]).__round__(1) for i in range(len(lstx))]
    syiDi=sum(yiDi)
    res = syiDi*Pnp1
    return res