from classes import Point, FoodLength
from collections import deque
from models import GameState, Snake, Food, Enemy
from typing import List
import numpy as np 
from math import sqrt, floor
import heapq



def find_orange(snake: Snake, array: np.ndarray, x_len:int, y_len:int, z_len:int) -> Point:
    elements = snake.geometry.copy()
    elements.reverse()
    first_element = elements.pop()
    elements.reverse()

    head = Point(first_element.root[0], first_element.root[1], first_element.root[2])
    body = []
    for i in elements:
        body.append(Point(i[0], i[1], i[2]))
    huy = deque()
    huy.append(head)
    result = None
    visited = []

    while huy:
        cur = huy.popleft()
        if cur in visited:
            continue

        if array[cur.x][cur.y][cur.z] > 1:
            for bod in body:
                if cur.x < bod.x or cur.y < bod.y or cur.z < bod.z:
                    continue
            result = cur
            break
        
        if x_len - 1 > cur.x + 1:
            huy.append(Point(cur.x+1, cur.y, cur.z))
        
        if y_len - 1 > cur.y + 1:
            huy.append(Point(cur.x, cur.y+1, cur.z))
        
        if z_len - 1 > cur.z + 1:
            huy.append(Point(cur.x, cur.y, cur.z+1))
        
        if cur.x - 1 < 0:
            huy.append(Point(cur.x-1, cur.y, cur.z))
        
        if cur.y - 1 < 0:
            huy.append(Point(cur.x, cur.y-1, cur.z))
        
        if cur.z - 1 < 0:
            huy.append(Point(cur.x, cur.y, cur.z-1))

        visited.append(cur)
    
    return result

def new_algo_find(snake: Snake, foods: list[Food]) -> FoodLength:
    elements = snake.geometry.copy()
    elements.reverse()
    first_element = elements.pop()
    elements.reverse()

    head = Point(first_element.root[0], first_element.root[1], first_element.root[2])
    result = []

    for food in foods:
        x = food.c.root[0]
        y = food.c.root[1]
        z = food.c.root[2]

        distance = sqrt(
            (x - head.x) ** 2 +
            (y - head.y) ** 2 +
            (z - head.z) ** 2
        )

        result.append(FoodLength(food=food, length=distance))

    return min(result, key=lambda obj : obj.length)


def find_nearest_safe_food(
    snake: Snake,  # Объект змейки
    array: np.ndarray,  # Карта
    x_len: int,  # Длина карты по x
    y_len: int,  # Длина карты по y
    z_len: int,  # Длина карты по z
    foods: list[Food]
) -> Point:
    def heuristic(a, b):
        """Эвристика: Манхэттенское расстояние между точками a и b."""
        return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

    def find_path(start, goals, max_depth=50):
        """
        Поиск пути с использованием A* до ближайшей цели из списка goals.
        Ограничение по глубине поиска (max_depth) для ускорения.
        """
        visited = set()
        queue = []
        heapq.heappush(queue, (0, start, 0))  # (стоимость, текущая точка, длина пути)

        while queue:
            cost, current, path_len = heapq.heappop(queue)
            if current in visited:
                continue
            visited.add(current)

            # Если достигли одной из целей
            if current in goals:
                return path_len, current

            # Ограничение по глубине
            if path_len > max_depth:
                continue

            x, y, z = current
            for dx, dy, dz in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
                nx, ny, nz = x + dx, y + dy, z + dz
                if 0 <= nx < x_len and 0 <= ny < y_len and 0 <= nz < z_len:
                    if (nx, ny, nz) not in visited and array[nx, ny, nz] >= 1:
                        new_cost = cost + 1
                        heapq.heappush(queue, (new_cost + heuristic((nx, ny, nz), goals[0]), (nx, ny, nz), path_len + 1))

        return float('inf'), None  # Если путь не найден

    def find_safe_point(start, max_depth=50):
        """
        Поиск ближайшей безопасной точки, ограниченной глубиной max_depth.
        """
        visited = set()
        queue = []
        heapq.heappush(queue, (0, start, 0))  # (стоимость, текущая точка, длина пути)

        while queue:
            cost, current, path_len = heapq.heappop(queue)
            if current in visited:
                continue
            visited.add(current)

            x, y, z = current
            if array[x, y, z] == 1:  # Безопасная точка
                return current

            # Ограничение по глубине
            if path_len > max_depth:
                continue

            for dx, dy, dz in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
                nx, ny, nz = x + dx, y + dy, z + dz
                if 0 <= nx < x_len and 0 <= ny < y_len and 0 <= nz < z_len:
                    if (nx, ny, nz) not in visited and array[nx, ny, nz] >= 0:
                        heapq.heappush(queue, (cost + 1, (nx, ny, nz), path_len + 1))

        return start  # Если безопасная точка не найдена, остаёмся на месте

    # Координаты головы змеи
    head = (snake.geometry[0].root[0], snake.geometry[0].root[1], snake.geometry[0].root[2])
    food_positions = [(food.c.root[0], food.c.root[1], food.c.root[2]) for food in foods]

    # Поиск пути до ближайшего мандарина
    path_len, best_food = find_path(head, food_positions)

    if best_food:
        return Point(best_food[0], best_food[1], best_food[2])
    else:
        # Если мандарин не найден, ищем безопасную точку
        safe_point = find_safe_point(head)
        return Point(safe_point[0], safe_point[1], safe_point[2])
    
def new_algo_find_v2(snake: Snake, foods: List[Food], enemies: List[Enemy]) -> FoodLength:
    elements = snake.geometry.copy()
    elements.reverse()
    first_element = elements.pop()
    elements.reverse()

    head = Point(first_element.root[0], first_element.root[1], first_element.root[2])
    result = []

    for food in foods:
        x = food.c.root[0]
        y = food.c.root[1]
        z = food.c.root[2]

        distance = _calculate_distance(x1=x, y1=y, z1=z, x2=head.x, y2=head.y, z2=head.z)

        result.append(FoodLength(food=food, length=floor(distance)))

    return _custom_min(result, enemies)

def _calculate_distance(x1, y1, z1, x2, y2, z2) -> float:
    return sqrt(
        (x1 - x2) ** 2 +
        (y1 - y2) ** 2 +
        (z1 - z2) ** 2
    )

def _custom_min(elems: List[FoodLength], enemies: List[Enemy]) -> FoodLength:
    result = elems[0]
    min_enemy_to_fruit = min(map(lambda x: _calculate_distance(result.food.c.root[0], result.food.c.root[1], result.food.c.root[2], x.geometry[0].root[0], x.geometry[0].root[1], x.geometry[0].root[2]), enemies))

    for i in range(1, len(elems)):
        cur_enemy_to_fruit = min(map(lambda x: _calculate_distance(elems[i].food.c.root[0], elems[i].food.c.root[1], elems[i].food.c.root[2], x.geometry[0].root[0], x.geometry[0].root[1], x.geometry[0].root[2]), enemies))
        
        if result.length > elems[i].length and min_enemy_to_fruit > cur_enemy_to_fruit:
            result = elems[i]
            min_enemy_to_fruit = cur_enemy_to_fruit

    return result