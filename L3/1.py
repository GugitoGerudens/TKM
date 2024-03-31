import matplotlib.pyplot as plt


class Pn:
    def __init__(self, y0):
        self.y0 = y0

    def f(self, x: float) -> float:
        u = x - 4
        i1 = 15 + 5 * u
        i2 = -1 / 4 * u * (u * u - 1) - 1 / 8 * u * u * (u * u - 1)
        i3 = 2 / 120 * u * (u * u - 1) * (u * u - 4) + 7 / 360 * u * u * (u * u - 1) * (u * u - 4)
        return i1 - i2 + i3

    @staticmethod
    def separated_differences(xs: list, ys: list):
        matrix = [[0] * 8 for _ in range(7)]

        for i, x in enumerate(xs):
            matrix[i][0] = x

        for i, y in enumerate(ys):
            matrix[i][1] = y

        for i in range(2, 8):
            for j in range(8 - i):
                matrix[j][i] = matrix[j + 1][i - 1] - matrix[j][i - 1]

        print('Промежуточные вычисления: ')
        print('x   y   Δ1y Δ2y Δ3y Δ4y Δ5y Δ6y')
        for i in matrix:
            for j in i:
                print(str(j).ljust(4), end='')
            print()


def main():
    xs = [0, 1, 2, 3, 4, 5, 6, 7]
    ys = [0, 2, 5, 10, 15, 20, 22, 24]

    x = 4.3

    x0_index = 5
    x0 = xs[x0_index]
    y0 = ys[x0_index]

    ex = Pn(y0)
    ex.separated_differences(xs[1:8], ys[1:8])

    y = ex.f(x)
    print()
    print('Ответ: ', y)

    fig, ax = plt.subplots()
    yss = list(map(ex.f, [i / 10 for i in range(70)]))
    ax.plot([i / 10 for i in range(70)][20:], yss[20:])
    print(yss)
    plt.show()


if __name__ == '__main__':
    main()
