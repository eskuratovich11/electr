import matplotlib.pyplot as plt

q_0 = 10
t_0 = 10
k = 0.05


def bac_func(q, t):
    return q * k


def euler(q_0=10, t_0=0, step=0.1, n=500):
    q = q_0
    t = t_0
    q_list = [q]
    t_list = [t]

    for _ in range(n):
        q = q + step * bac_func(q, t)
        t = t + step
        q_list.append(q)
        t_list.append(t)
    return t_list, q_list


solve = euler(q_0, t_0)
plt.plot(solve[0], solve[1])
plt.show()
# n - количество итераций, h - шаг, (x, y) - начальная точка
def Euler(n = 10, h = 0.01, x0 = 1, y0 = 1):
    x = x0
    y = y0
    x_list = [x]
    y_list = [y]
    for i in range(n):

        y += y0+ h * function(x, y)
        x += x0+  h
        x_list.append(x)
        y_list.append(y)

    return x_list, y_list  # решение

def function(x, y):
    return 6 * x**2 + 5 * x * y # функция первой производной

print(Euler())
