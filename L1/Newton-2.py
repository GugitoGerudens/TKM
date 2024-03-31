import math


def Pn1(arg, x0, x, y):
    x0i=x.index(x0)
    dy=[]
    dy.append([round(y[i]-y[i-1],4) for i in range(1, len(y))])
    dy.append([round(dy[0][i]-dy[0][i-1],4) for i in range(1, len(dy[0]))])
    dy.append([round(dy[1][i]-dy[1][i-1],4) for i in range(1, len(dy[1]))])
    q = (arg-x0)/(x[1]-x[0])
    s = y[x0i]
    for i in range(3):
        s+=q*dy[i][x0i]/math.factorial(i+1)
        q*=(q-1)
    return s

def Pn2(x,y):
    dy = []
    dy.append([round(y[i] - y[i - 1], 4) for i in range(1, len(y))])
    dy.append([round(dy[0][i] - dy[0][i - 1], 4) for i in range(1, len(dy[0]))])
    return(f"{y[0]}{'+' if dy[0][0]>=0 else '-'}{abs(dy[0][0])}x{'+' if dy[1][0]>=0 else '-'}{abs(dy[1][0]/2)}x^2")

if __name__ == "__main__":
    print(Pn1(1.43, 1.4, [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0],
              [0.8427, 0.8802, 0.9103, 0.934, 0.9523, 0.9661, 0.9763, 0.9838, 0.9891, 0.9928, 0.9953]))
    print(Pn2([0, 1, 2, 3, 4, 5], [5.2, 8.0, 10.4, 12.4, 14.0, 15.2]))
