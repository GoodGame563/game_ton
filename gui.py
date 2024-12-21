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
# visualize_3d_array_with_animation()
# Определение цветовой карты
def get_color(value):
    if value > 1:
        return (1, 1, 0)  # Желтый
    elif value == 0:
        return (0, 0, 0)  # Черный
    elif value == -2:
        return (0, 0, 1)  # Синий
    elif value == -1:
        return (1, 0, 0)  # Красный
    elif value < -2:
        return (1, 0.5, 0)  # Оранжевый
    else:
        return None  # Для значения 1 не будем отображать точку

# Визуализация всего 3D массива
def visualize_3d_array(array):
    x_dim, y_dim, z_dim = array.shape
    fig = plt.figure(figsize=(16, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Массивы для координат
    x_vals, y_vals, z_vals, colors = [], [], [], []

    # Проход по всему массиву для сбора координат и цветов
    for x in range(x_dim):
        for y in range(y_dim):
            for z in range(z_dim):
                value = array[x, y, z]
                color = get_color(value)
                if color is not None:
                    x_vals.append(x)
                    y_vals.append(y)
                    z_vals.append(z)
                    colors.append(color)

    # Преобразуем списки в массивы для scatter
    x_vals = np.array(x_vals)
    y_vals = np.array(y_vals)
    z_vals = np.array(z_vals)
    colors = np.array(colors)

    # Отображение точек с нужными цветами
    ax.scatter(x_vals, y_vals, z_vals, c=colors, marker='o', s=2)
    
    # Настройка осей и отображение
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Visualization of Array (No White)')

    plt.show()

gs = get_map()
if gs is None:
    with open('data.json') as file:
        gs = GameState(**json.load(file))
arr = return_fields(gs)
visualize_3d_array(arr)

