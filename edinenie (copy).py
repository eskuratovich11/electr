import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frame = 5000
seconds_in_year = 365 * 24 * 60 * 60
years = 0.1
t = np.linspace(0, years * seconds_in_year, frame)

G = 6.67 * 10 ** (-11)
k = 8.98755 * 10 ** 9
N = 0

def getter(variable_balls, num):
    """
    :param variable_balls - все объекты моделирования
    :param num - номер объекта на который дейсвуют другие тела
    :return out: взаимодействие variable_balls элементов на num-ый элемент по x
    """
    global out_x, out_y
    out_x = 0.0
    out_y = 0.0
    for i in range(N):
        if i != num:
            # Вычисляем гравитационное взаимодействие variable_balls элементов на num-ый элемент
            out_x += (-G * not_variable_balls[i * 2 + 0] *
                    (variable_balls[num * 4 + 0] - variable_balls[i * 4 + 0]) /
                    ((variable_balls[num * 4 + 0] - variable_balls[i * 4 + 0]) ** 2 + (
                            variable_balls[num * 4 + 2] - variable_balls[i * 4 + 2]) ** 2) ** 1.5)

            # Вычисляем взаимодействие заряженных тел variable_balls элементов на num-ый элемент
            out_x += (k *
                    not_variable_balls[num * 2 + 1] * not_variable_balls[i * 2 + 1] /
                    not_variable_balls[num * 2 + 0] *
                    (variable_balls[num * 4 + 0] - variable_balls[i * 4 + 0]) /
                    ((variable_balls[num * 4 + 0] - variable_balls[i * 4 + 0]) ** 2 + (
                            variable_balls[num * 4 + 2] - variable_balls[i * 4 + 2]) ** 2) ** 1.5)

            # Вычисляем гравитационное взаимодействие variable_balls элементов на num-ый элемент
            out_y += (-G * not_variable_balls[i * 2 + 0] *
                    (variable_balls[num * 4 + 2] - variable_balls[i * 4 + 2]) /
                    ((variable_balls[num * 4 + 0] - variable_balls[i * 4 + 0]) ** 2 + (
                            variable_balls[num * 4 + 2] - variable_balls[i * 4 + 2]) ** 2) ** 1.5)

            # Вычисляем взаимодействие заряженных тел variable_balls элементов на num-ый элемент
            out_y += (k *
                    not_variable_balls[num * 2 + 1] * not_variable_balls[i * 2 + 1] /
                    not_variable_balls[num * 2 + 0] *
                    (variable_balls[num * 4 + 2] - variable_balls[i * 4 + 2]) /
                    ((variable_balls[num * 4 + 0] - variable_balls[i * 4 + 0]) ** 2 + (
                            variable_balls[num * 4 + 2] - variable_balls[i * 4 + 2]) ** 2) ** 1.5)
    return out_x , out_y





not_variable_balls = []

# Лист изменяемых данных моделируемых объектов
# Период = 4
# Данные одного моделируемого объекта: 0 = x, 1 = вектор x, 2 = y, 3 = вектор y
variable = []


def ball(mas, electric_charge, x0, v_x0, y0, v_y0):
    """
    Распределяет данные моделируемых объктов по листам
    :param mas: масса
    :param electric_charge: электрический заряр
    :param x: координата x
    :param v_x: вектор по x
    :param y: координата y
    :param v_y: вектор по y
    """
    not_variable_balls.append(mas)
    not_variable_balls.append(electric_charge)
    variable.append(x0)
    variable.append(v_x0)
    variable.append(y0)
    variable.append(v_y0)


# Добавляем объекты моделирования
ball(1.1 * 10 ** 30, 1.1 * 10 ** 20, 149 * 10 ** 8, 0, 0, 30000)
ball(2.1 * 10 ** 30, 2.1 * 10 ** 20, - 149 * 10 ** 8, 1, 0, -30000)
ball(3.6 * 10 ** 30, -3.1 * 10 ** 20, 0, 15000, 149 * 10 ** 8, 0)
ball(7 * 10 ** 30, -2.6 * 10 ** 20, 0, 0, 0, 0)

# Вычисляем сколько всего мы моделируем объектов
N = int(len(not_variable_balls) / 2)
x_0= variable[2]
y_0= variable[4]
t_0=0

def euler(x_0, y_0,  t_0,  variable_balls=, num , step=0.1, n=500):
    x = x_0
    y= y_0
    t = t_0
    x_list = [x]
    y_list=[y]   
    t_list = [t]

    for _ in range(n):
        x= x+ step * getter(variable_balls, num)
        y = y + step * getter(variable_balls, num)  
        t = t + step
        x_list.append(x)
        y_list.append(y)
        t_list.append(t)

    return x_list, y_list, t_list

# Моделируем
sol = euler (x_0, y_0,  t_0,  variable_balls, num )


def solve_func(i, n, key):
    """
    :param i: время в которое мы берём координаты
    :param n: номер моделируемого объекта для которого мы получаем координаты
    :param key: ключь. Если key="point", то получам координаты для моделирования точьки
        в ином случае получае координаты для моделирования пути моделирукмого объекта
    :return x, y: n-го моделируемого элемента в i-е время
    """

    if key == "point":
        x = sol[i, n * 4 + 0]
        y = sol[i, n * 4 + 2]
    else:
        x = sol[:i, n * 4 + 0]
        y = sol[:i, n * 4 + 2]

    return x, y


fig, ax = plt.subplots()

# Лист графических элементов моделируемых объектов
# Переод = 2
# Данные одного моделируемого объекта: 0 = шар, 1 = путь
plots = []

# Создаём для каждего моделируемого объекта графические элементы
for i in range(N):
    # создаём рандомный цвет
    colors = np.random.rand(3, )

    # создаём графический элемент "шар"
    plot, = plt.plot([], [], 'o', c=colors, ms=5)
    plots.append(plot)

    # создаём графический элемент "лия"
    plot2, = plt.plot([], [], '-', c=colors)
    plots.append(plot2)


def animate(i):
    """
    Моделируем для каждего моделируемого объека графические элементы
    :param i: время в которое мы берём координаты
    """

    for j in range(N):
        plots[j * 2 + 0].set_data(solve_func(i, j, 'point'))
        plots[j * 2 + 1].set_data(solve_func(i, j, 'line'))

ani = FuncAnimation(fig,
                    animate,
                    frames=500,
                    interval=30)

plt.axis('equal')
edge = 2 * 300 * 10 ** 8
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

plt.show()