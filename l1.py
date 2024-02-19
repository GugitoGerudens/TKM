import math
import matplotlib.pyplot
def interpol(x, lstx, lsty, debug=False):
    Pnp1 =  math.prod([(x - lstx[i]) for i in range(len(lstx))])
    di=[[(lstx[i] if i!=j else x)-lstx[j] for j in range(len(lstx))] for i in range(len(lstx))]
    Di=[math.prod(di[i]) for i in range(len(lstx))]
    yiDi = [(lsty[i] / Di[i]).__round__(1) for i in range(len(lstx))]
    syiDi=sum(yiDi)
    res = syiDi*Pnp1
    return res
#print(interpol(0.263, [0.05, 0.1, 0.17, 0.25, 0.3, 0.36], [0.050042, 0.100335, 0.171657, 0.255342, 0.309336, 0.376403],False))
print(interpol(0.1157, [0.101, 0.106, 0.111, 0.116, 0.121, 0.126],[1.26183, 1.27644, 1.29122, 1.30617, 1.32130, 1.32660]))