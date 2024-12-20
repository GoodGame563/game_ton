import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Визуализатор с анимацией
def visualize_3d_array_with_animation():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Инициализация точек
    x_coords = []
    y_coords = []
    z_coords = []
    colors = []

    # Функция для обновления графика на каждом кадре анимации
    def update_plot():
        # Получаем массив данных через return_fields
        gs = 
        arr = return_fields(gs)
        
        # Очищаем текущие данные
        ax.cla()

        # Списки для новых координат и цветов
        x_coords.clear()
        y_coords.clear()
        z_coords.clear()
        colors.clear()
        
        # Заполнение данных
        x_len, y_len, z_len = arr.shape
        for x in range(x_len):
            for y in range(y_len):
                for z in range(z_len):
                    value = arr[x, y, z]
                    if value == -1:
                        x_coords.append(x)
                        y_coords.append(y)
                        z_coords.append(z)
                        colors.append('b')  # синий для -1
                    elif value == 0:
                        x_coords.append(x)
                        y_coords.append(y)
                        z_coords.append(z)
                        colors.append('k')  # черный для 0
                    elif value == -2:
                        x_coords.append(x)
                        y_coords.append(y)
                        z_coords.append(z)
                        colors.append('r')  # красный для -2
                    elif value == 2:
                        x_coords.append(x)
                        y_coords.append(y)
                        z_coords.append(z)
                        colors.append('y')  # желтый для 2
        
        # Отображаем новые точки
        ax.scatter(x_coords, y_coords, z_coords, c=colors, marker='o')

        # Оформляем график
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(f'Frame {gs}')

    # Создание анимации
    ani = FuncAnimation(fig, update_plot, frames=10, interval=1000, repeat=True)

    plt.show()

# Запуск анимации
visualize_3d_array_with_animation()
