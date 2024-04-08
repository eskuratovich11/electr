import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Создаем фигуру и оси
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
r1 = 3
r2 = 5
r3= 6.5
# Инициализация положения частиц
proton1 = ax.scatter(0.45, 0.45, color='red', s=100)
proton2 = ax.scatter(0.45, -0.45, color='red', s=100)
proton3 = ax.scatter(-0.45, 0.45, color='red', s=100)
proton4 = ax.scatter(-0.45, -0.45, color='red', s=100)
neutron1 = ax.scatter(0.6, 0, color='grey', s=100)
neutron2 = ax.scatter(0, 0.6, color='grey', s=100)
neutron3 = ax.scatter(-0.6, 0, color='grey', s=100)
neutron4 = ax.scatter(0, -0.6, color='grey', s=100)
neutron5 = ax.scatter(0, 0, color='grey', s=100)
electron1 = ax.scatter(r1,0, color='blue', s=50)
electron2 = ax.scatter(r2,0, color='blue', s=50)
electron3 = ax.scatter(r3,0, color='blue', s=50)

# Настройка анимации
def update(frame):
    # Обновление положения электронов
    electron1.set_offsets([np.cos(frame + np.pi / 180) * r1, np.sin(frame + np.pi / 180) * r1])
    electron2.set_offsets([np.cos(frame + np.pi / 180) * r2, np.sin(frame + np.pi / 180) * r2])
    electron3.set_offsets([np.cos(frame + np.pi / 180) * r3, np.sin(frame + np.pi / 180) * r3])
    return electron1,electron2,electron3

# Создаем анимацию
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 360), interval=50, blit=True)

# Сохраняем анимацию в файл gif
ani.save('atom_animation.gif', writer='pillow', fps=30)