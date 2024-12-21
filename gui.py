import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from api_connect import get_map
from field import return_fields
from models import GameState
import json

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
    def update_plot(rofl):
        # Получаем массив данных через return_fields
        gs = get_map()
        if gs is None:
            with open('data.json') as file:
                gs = GameState(**json.load(file))
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

        # Установка пределов осей на основе gs.mapSize
        map_size = gs.mapSize
        # ax.set_xlim(0, map_size[0])
        # ax.set_ylim(0, map_size[1])
        # ax.set_zlim(0, map_size[2])

        # Оформляем график
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

    # Создание анимации
    ani = FuncAnimation(fig, update_plot, frames=10, interval=5000, repeat=True)

    plt.show()

# Запуск анимации
visualize_3d_array_with_animation()
