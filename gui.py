import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from api_connect import get_map
from field import return_fields
from models import GameState
import json
import time
# Визуализатор с анимацией
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
    
def load_game_state():
    with open('data.json') as file:
        return GameState(**json.load(file))
    
def visualize_3d_array_with_animation():
    fig = plt.figure(figsize=(16, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Настройка осей
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Visualization of Array with Animation')

    # Инициализация пустого scatter-объекта для анимации
    scatter = ax.scatter([], [], [], c=[], marker='o', s=2)

    # Функция для обновления данных в анимации
    def update(frame):
        # Получаем обновленное состояние игры
        gs = get_map()
        if gs is None:
            print("get_map() returned None. Loading game state from file...")
            gs = load_game_state()  # Загружаем состояние игры из файла, если get_map() вернул None
        
        arr = return_fields(gs)

        # Проверим, что return_fields вернуло данные
        print(f"Shape of the array from return_fields: {arr.shape}")
        
        # Собираем координаты и цвета для точек
        x_vals, y_vals, z_vals, colors = [], [], [], []
        x_dim, y_dim, z_dim = arr.shape

        for x in range(x_dim):
            for y in range(y_dim):
                for z in range(z_dim):
                    value = arr[x, y, z]
                    color = get_color(value)
                    if color is not None:
                        x_vals.append(x)
                        y_vals.append(y)
                        z_vals.append(z)
                        colors.append(color)

        # Проверим, сколько точек мы добавили
        print(f"Number of points to display: {len(x_vals)}")

        if len(x_vals) == 0:
            print("No points to display.")
            return

        # Преобразуем списки в массивы для scatter
        x_vals = np.array(x_vals)
        y_vals = np.array(y_vals)
        z_vals = np.array(z_vals)
        colors = np.array(colors)

        # Обновляем scatter с новыми данными
        scatter._offsets = np.column_stack([x_vals[:frame], y_vals[:frame], z_vals[:frame]])
        scatter.set_color(colors[:frame])

    # Создание анимации
    ani = FuncAnimation(fig, update, frames=500, interval=1000, repeat=True)

    # Отображение анимации
    plt.show()
# Пример использования:
# visualize_3d_array_with_animation()
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
# visualize_3d_array(arr)

