import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Solver:
    def __init__(self, data_objects ):
        self.data_objects = data_objects

        self.frame = 5000
        self.seconds_in_year = 365 * 24 * 60 * 60
        self.years = 0.1
        self.t = np.linspace(0, self.years * self.seconds_in_year, self.frame)

        self.G = 6.67 * 10 ** (-11)
        self.k = 8.98755 * 10 ** 9
        
        self.N = int(len(self.data_objects))

        # Лист не изменяемых данных моделируемых объектов
        # Период = 2
        # Данные одного моделируемого объекта: 0 = масса, 1 = заряд
        self.not_variable_balls = []

        # Лист изменяемых данных моделируемых объектов
        # Период = 4
        # Данные одного моделируемого объекта: 0 = x, 1 = вектор x, 2 = y, 3 = вектор y
        self.variable = []

    """
    ################### Логика построения list[n * a + b] ###################
    n - элемент который мы хотим получить
    a - период list
    Период - это количесво вставляемых подряд данных одного объекта моделирования в определённый лист
    b - какие данные элемента мы хотим получить
    """



    def get_dv_dt(self, variable_balls, num, key):
        """
        :param variable_balls - все объекты моделирования
        :param num - номер объекта на который дейсвуют другие тела
        :param key - компонента скорость 'vx' или 'vy'
        :return out: взаимодействие variable_balls элементов на num-ый элемент по x
        """

        out = 0.0

        if key == 'vx':
            component = 0
        else:
            component = 2

        for i in range(self.N):
            if i != num:
                # Вычисляем гравитационное взаимодействие variable_balls элементов на num-ый элемент
                out += (-self.G * self.not_variable_balls[i * 2 + 0] *
                        (self.variable_balls[num * 4 + component] - self.variable_balls[i * 4 + component]) /
                        ((self.variable_balls[num * 4 + 0] - self.variable_balls[i * 4 + 0]) ** 2 + (
                                self.variable_balls[num * 4 + 2] - self.variable_balls[i * 4 + 2]) ** 2) ** 1.5)

                # Вычисляем взаимодействие заряженных тел variable_balls элементов на num-ый элемент
                out += (self.k *
                        self.not_variable_balls[num * 2 + 1] * self.not_variable_balls[i * 2 + 1] /
                        self.not_variable_balls[num * 2 + 0] *
                        (self.variable_balls[num * 4 + component] - self.variable_balls[i * 4 + component]) /
                        ((self.variable_balls[num * 4 + 0] - self.variable_balls[i * 4 + 0]) ** 2 + (
                                self.variable_balls[num * 4 + 2] - self.variable_balls[i * 4 + 2]) ** 2) ** 1.5)
        return out

    def move_func(self):
        """
        :param variable: все изменияемые данные объектов моделирования
        :param t: linspace переода времяни
        :return: outs: решение диференциального уравнения
        """

        # Лист возвращяемых данных
        # Период = 4
        # Элементы объекта: 0 = dxdt, 1 = dv_xdt, 2 = dydt, 3 = dv_ydt
        outs = []

        # Для каждего моделируемого объекта вычислем возвращяемые даннные
        for j in range(self.N):
            # Вычисляем dxdt
            outs.append(self.variable[j * 4 + 1])
            # Вычисляем dv_xdt
            outs.append(self.get_dv_dt(self.variable, j, 'vx'))
            # Вычисляем dydt
            outs.append(self.variable[j * 4 + 3])
            # Вычисляем dv_ydt
            outs.append(self.get_dv_dt(self.variable, j, 'vy'))

        return outs

    def ball( self ):
      """
      Распределяет данные моделируемых объктов по листам
      :param mas: масса
      :param electric_charge: электрический заряр
      :param x: координата x
      :param v_x: вектор по x
      :param y: координата y
      :param v_y: вектор по y
      """
  
      # 0 mas, 1 electric_charge, 2 x, 3 v_x, 4 y,5 v_y
      self.not_variable_balls.append(self.data_objects[0])
      self.not_variable_balls.append(self.data_objects[1])
      self.variable.append(self.data_objects[2])
      self.variable.append(self.data_objects[3])
      self.variable.append(self.data_objects[4])
      self.variable.append(self.data_objects[5])
      self.N = int(len(self.not_variable_balls) / 2)
  
    # Добавляем объекты моделирования
    # [[x0, vx0, y0, vy0, m0, q0],
    #  [x1, vx1, y1, vy0, m0, q0],
    #  [x1, vx1, y1, vy0, m0, q0]]
      
    def data_func(self):
      for i in range(len(self.data_objects)):
          for j in range(6):
              self.ball(self.data_objects[i, j])





    # Вычесляем сколько всего мы моделируем объектов


    # Моделируем


      
    def solve_func(self, i, n, key):
        """
        :param i: время в которое мы берём координаты
        :param n: номер моделируемого объекта для которого мы получаем координаты
        :param key: ключь. Если point то получам координаты для моделирования точьки
            в ином случае получае координаты для моделирования пути моделирукмого объекта
        :return x, y: n-го моделируемого элемента в i-е время
        """
        sol = odeint(self.move_func(), self.variable, self.t)
      
        if key == "point":
            x = sol[i, n * 4 + 0]
            y = sol[i, n * 4 + 2]
        else:
            x = sol[:i, n * 4 + 0]
            y = sol[:i, n * 4 + 2]

        return x, y

  


        
balls = Solver ([[ 1.1 * 10 ** 30, 1.1 * 10 ** 20, 149 * 10 ** 8, 0, 0, 30000],[2.1 * 10 ** 30, 2.1 * 10 ** 20, - 149 * 10 ** 8, 1, 0, -30000]])


fig, ax = plt.subplots()
      # Лист графических элементов моделируемых объектов
      # Период = 2
      # Данные одного моделируемого объекта: 0 = шар, 1 = путь
plots = []
      # Создаём для каждего моделируемого объекта графические элементы
for i in range(balls.N):
    # создаём рандомный цвет
    colors = np.random.rand(3, )
    # создаём графический элемент "шар"
    plot, = plt.plot([], [], 'o', c=colors, ms=5)
    plots.append(plot)
    # создаём графический элемент "линия"
    plot2, = plt.plot([], [], '-', c=colors)
    plots.append(plot2)
  
def animate(i):
  for j in range(balls.N):
      plots[j * 2 + 0].set_data(balls.solve_func(i, j, 'point'))
      plots[j * 2 + 1].set_data(balls.solve_func(i, j, 'line'))

ani = FuncAnimation(fig,
                    animate,
                    frames=500,
                    interval=30)
plt.axis('equal')
edge = 2 * 300 * 10 ** 8
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
plt.show()
