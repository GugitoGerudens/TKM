import matplotlib.pyplot as plt


def f(x: int) -> int:
    return x * x


def lagrange(x):
    return (x - 0) * (x - 1) / (-1 - 0) / (-1 - 1) + (x + 1) * (x - 0) / (1 + 1) * (1 - 0)


if __name__ == '__main__':
    index = list(range(0, 3))
    print('Индекс:', *index)

    xs = [-1, 0, 1]
    print('x:    ', *xs)

    ys = list(map(f, xs))
    print('y:     ', *ys)

    xss = [i / 100 for i in range(-100, 101)]
    yss = list(map(lagrange, xss))
    print(xss)
    print(yss)

    fig, ax = plt.subplots()
    ax.plot(xss, yss)
    plt.show()