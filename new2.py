import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Создаем фигуру и оси
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Координаты ядра атома
proton1 = np.array([0, 0, 0.1])
proton2 = np.array([0, 0, -0.1])
proton3 = np.array([0, 0.1, 0])
proton4 = np.array([0, -0.1,0])

neutron1 = np.array([0, 0, 0])
neutron2 = np.array([0.1, 0, 0.1])
neutron3 = np.array([-0.1, 0, -0.1])
neutron4 = np.array([-0.1, 0, 0.1])
neutron5 = np.array([0.1, 0, -0.1])
# Координаты электронов
electron1 = np.array([1, 0, 0])
electron2 = np.array([0, 2, 0])
electron3 = np.array([0, 3, 3])
electron3 = np.array([1, 0, 0.5])
# Построение ядра
ax.scatter(*proton1, color='red', label='Протон',  s=50)
ax.scatter(*neutron1, color='gray', label='Нейтрон',  s=50)
ax.scatter(*proton2, color='red',  s=50)
ax.scatter(*neutron2, color='gray',   s=50)
ax.scatter(*proton3, color='red', s=50)
ax.scatter(*neutron3, color='gray',  s=50)
ax.scatter(*proton4, color='red', s=50)
ax.scatter(*neutron4, color='gray',   s=50)
ax.scatter(*neutron5, color='gray',   s=50)
# Построение электронов
elec1, = ax.plot([], [], [], 'bo-', label='Электрон 1')
elec2, = ax.plot([], [], [], 'bo-', label='Электрон 2')
elec3, = ax.plot([], [], [], 'bo-', label='Электрон 3')
elec4, = ax.plot([], [], [], 'bo-', label='Электрон 4')
# Функция для обновления координат электронов
def update(frame):
    angle = frame * np.pi / 180
    radius1 = 1
    radius2 = 0.4
    radius3 = 0.5
    radius4 = 0.7
    elec1.set_data(radius1 * np.cos(angle), radius1 * np.sin(angle))
    elec2.set_data(radius2 * np.cos(angle + np.pi/2), radius2 * np.sin(angle + np.pi/2))
    elec3.set_data(radius3 * np.cos(angle + np.pi/4), radius3 * np.sin(angle + np.pi/4))
    elec4.set_data(radius4 * np.cos(angle - np.pi/2), radius4 * np.sin(angle - np.pi/2))
    elec1.set_3d_properties([0])
    elec2.set_3d_properties([0])
    elec3.set_3d_properties([0])
    elec4.set_3d_properties([0])
    return elec1, elec2, elec3,elec4

# Создание анимации
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50, blit=True)

# Настройка осей и отображение легенды
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
ax.legend()

# Сохранение анимации в файл gif
ani.save('atom_animation2.gif', writer='pillow')
