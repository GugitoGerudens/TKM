import matplotlib.pyplot as plt


def func_val(y_zero, first_order_diff, x_val, x_zero, second_order_diff, x_one):
    diff = x_val - x_zero
    result = y_zero + first_order_diff * diff + second_order_diff * diff * (x_val - x_one)
    return round(result, 5)


def newton_inter(arr_x, arr_y, x_val):
    n = len(arr_x)
    first_order_diff = [None] * (n-1)
    second_order_diff = [None] * (n-2)
    for i in range(0, n-1):
        first_order_diff[i] = (arr_y[i+1]-arr_y[i])/(arr_x[i+1]-arr_x[i])
    for i in range(0, n-2):
        second_order_diff[i] = (first_order_diff[i+1]-first_order_diff[i])/(arr_x[i+2]-arr_x[i])
    num = 0
    for i in range(0, n-1):
        if x_val > arr_x[i]:
            num = i
        else:
             break
    res_2 = func_val(arr_y[num], first_order_diff[num], x_val, arr_x[num], second_order_diff[num], arr_x[num+1])
    num -= 1
    res_1 = 0
    if num >= 0:
        res_1 = func_val(arr_y[num], first_order_diff[num], x_val, arr_x[num], second_order_diff[num], arr_x[num+1])
    answer = (res_1 + res_2)/2
    return answer, num+2


def main():
    x = [0.103, 0.108, 0.115, 0.120, 0.128, 0.136, 0.141, 0.150]
    y = [2.01284, 2.03342, 2.06070, 2.07918, 2.10721, 2.13354, 2.14922, 2.17609]
    first_x = 0.112
    second_x = 0.133
    answer_1 = newton_inter(x, y, first_x)
    answer_2 = newton_inter(x, y, second_x)
    print('Ответ:')
    print('f(', first_x, ') = ', answer_1[0])
    print('f(', second_x, ') = ', answer_2[0])

    # printing
    x.insert(answer_1[1], first_x)
    x.insert(answer_2[1]+1, second_x)
    y.insert(answer_1[1], answer_1[0])
    y.insert(answer_2[1]+1, answer_2[0])

    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()


if __name__ == "__main__":
    main()
