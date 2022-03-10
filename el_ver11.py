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
        self.N = 0

        # Лист не изменяемых данных моделируемых объектов
        # Период = 2
        # Данные одного моделируемого объекта: 0 = масса, 1 = зарят
        self.not_variable_balls = []

        # Лист изменяемых данных моделируемых объектов
        # Период = 4
        # Данные одного моделируемого объекта: 0 = x, 1 = вектор x, 2 = y, 3 = вектор y
        self.variable = []

    """
    ################### Логика построения list[n * a + b] ###################
    n - элемент который мы хотим получить
    a - период list
    Период - это количесво вставляемых подрят данных одного объекта моделирования в определённый лист
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
    
    '''
    def odeint_eiler(self):
        x0 = []
        for i in range(len(self.data_objects)):
            x0.append(self.move_func(self.variable, self.t)[j * 4 + 1])

        for i in range(len(self.t)):
            x1 = x0 + t[i] * vx0
            vx1 = vx0 + t[i] * self.get_dv_dt(vx0, j, 'vx')
            y1 = y0 + t[i] * vy0
            vy1 = vy0 + t[i] * self.get_dv_dt(vy0, j, 'vx')

            x0 = x1
            vx0 = vx1
            y0 = y1
            vy0 = vy1

        return x, y

        # x = [[x1ball1, x2ball1, ..., x5000ball1],
        #      [x1ball2, x2ball2, ..., x5000ball2]]
    '''
    def sol (self):
      self.sol = odeint(self.move_func(), self.variable, self.t)
      return self.sol
    def solve_func(self, i, n, key):
        """
        :param i: время в которое мы берём координаты
        :param n: номер моделируемого объекта для которого мы получаем координаты
        :param key: ключь. Если point то получам координаты для моделирования точьки
            в ином случае получае координаты для моделирования пути моделирукмого объекта
        :return x, y: n-го моделируемого элемента в i-е время
        """
        
        if key == "point":
            x = self.sol[i, n * 4 + 0]
            y = self.sol[i, n * 4 + 2]
        else:
            x = self.sol[:i, n * 4 + 0]
            y = self.sol[:i, n * 4 + 2]

        return x, y

  
    def plots(self, i):
      self.fig, self.ax = plt.subplots()
      # Лист графических элементов моделируемых объектов
      # Период = 2
      # Данные одного моделируемого объекта: 0 = шар, 1 = путь
      self.plots = []
      # Создаём для каждего моделируемого объекта графические элементы
      for i in range(Solver.N):
          # создаём рандомный цвет
          colors = np.random.rand(3, )
          # создаём графический элемент "шар"
          plot, = plt.plot([], [], 'o', c=colors, ms=5)
          self.plots.append(plot)
          # создаём графический элемент "линия"
          plot2, = plt.plot([], [], '-', c=colors)
          self.plots.append(plot2)
        
    def animate(self, i, j):
      for j in range(self.N):
          self.plots[j * 2 + 0].set_data(self.solve_func(i, j, 'point'))
          self.plots[j * 2 + 1].set_data(self.solve_func(i, j, 'line'))
    def show(self,i):
      self.ani = FuncAnimation(self.fig,
                          self.animate(i),
                          frames=500,
                          interval=30)
      plt.axis('equal')
      edge = 2 * 300 * 10 ** 8
      self.ax.set_xlim(-edge, edge)
      self.ax.set_ylim(-edge, edge)

        
ball1 = Solver ([ 1.1 * 10 ** 30, 1.1 * 10 ** 20, 149 * 10 ** 8, 0, 0, 30000])
ball2 = Solver([2.1 * 10 ** 30, 2.1 * 10 ** 20, - 149 * 10 ** 8, 1, 0, -30000])
ball3 = Solver( [3.6 * 10 ** 30, -3.1 * 10 ** 20, 0, 15000, 149 * 10 ** 8, 0])
ball4 = Solver( [7 * 10 ** 30, -2.6 * 10 ** 20, 0, 0, 0, 0])
ball5 = Solver( [7 * 10 ** 30, -2.6 * 10 ** 20, 349 * 10 ** 8, 0, 0, 0])

plt.show()


