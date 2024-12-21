from enum import Enum
from classes import Point
from models import Snake
import numpy as np
from math import sqrt
from collections import deque
import heapq

def move(snake: Snake, orange: Point, field: np.ndarray, x_len:int, y_len:int, z_len:int) -> Point:
    elements = snake.geometry.copy()
    elements.reverse()
    first_element = elements.pop()
    elements.reverse()
    head = Point(first_element.root[0], first_element.root[1], first_element.root[2])
    body = []
    for i in elements:
        body.append(Point(i.root[0], i.root[1], i.root[2]))

    result = Point(head.x, head.y, head.z)

    def is_valid_move(next_point: Point):
        return (
            0 <= next_point.x < x_len and
            0 <= next_point.y < y_len and
            0 <= next_point.z < z_len and
            field[next_point.x][next_point.y][next_point.z] != 0 and
            _check_body(body, next_point) and field[next_point.x][next_point.y][next_point.z] != -2 and field[next_point.x][next_point.y][next_point.z] > -2
        )

    def distance_to_goal(point: Point):
        return sqrt(
            (orange.x - point.x) ** 2 +
            (orange.y - point.y) ** 2 +
            (orange.z - point.z) ** 2
        )

    neighbors = [
        Point(head.x + 1, head.y, head.z),
        Point(head.x - 1, head.y, head.z),
        Point(head.x, head.y + 1, head.z),
        Point(head.x, head.y - 1, head.z),
        Point(head.x, head.y, head.z + 1),
        Point(head.x, head.y, head.z - 1),
    ]

    valid_neighbors = [p for p in neighbors if is_valid_move(p)]
    print(len(valid_neighbors))

    if valid_neighbors:
        result = min(valid_neighbors, key=distance_to_goal)
    else:
        result = head

    return result - head


def _check_body(body, next_point):
    return next_point not in body

def find_path(snake: Snake, orange: Point, field: np.ndarray, x_len: int = 180, y_len: int = 180 , z_len: int = 60) -> list[Point]:
    head = Point(snake.geometry[0].root[0], snake.geometry[0].root[1], snake.geometry[0].root[2])
    
    directions = [
        (1, 0, 0), (-1, 0, 0),  # движение по оси x
        (0, 1, 0), (0, -1, 0),  # движение по оси y
        (0, 0, 1), (0, 0, -1)   # движение по оси z
    ]
    
    def is_valid_move(point: Point):
        return (0 <= point.x < x_len and 
                0 <= point.y < y_len and 
                0 <= point.z < z_len and 
                field[point.x][point.y][point.z] == 1 and  # клетка должна быть свободной (значение 1)
                point not in [Point(seg.root[0], seg.root[1], seg.root[2]) for seg in snake.geometry])

    def bfs(start: Point, goal: Point):
        queue = deque([(start, [])])  # очередь, хранящая текущую точку и путь до неё
        visited = set()  # множество посещённых точек
        visited.add((start.x, start.y, start.z))  # добавляем стартовую точку в посещённые
        
        while queue:
            current_point, path = queue.popleft()
            
            # Если мы достигли цели, возвращаем путь
            if current_point == goal:
                return path + [current_point]
            
            # Проверка всех соседей
            for dx, dy, dz in directions:
                neighbor = Point(current_point.x + dx, current_point.y + dy, current_point.z + dz)
                
                # Если сосед допустим, добавляем его в очередь
                if is_valid_move(neighbor) and (neighbor.x, neighbor.y, neighbor.z) not in visited:
                    visited.add((neighbor.x, neighbor.y, neighbor.z))
                    queue.append((neighbor, path + [current_point]))
        
        return [] 
    
    return bfs(head, orange)

def find_optimal_path(snake: Snake, goal: Point, field: np.ndarray, x_len: int, y_len: int, z_len: int) -> list[Point]:
    start = Point(snake.geometry[0].root[0], snake.geometry[0].root[1], snake.geometry[0].root[2])
    # Направления движения по осям x, y, z
    directions = [
        (1, 0, 0), (-1, 0, 0),  # движение по оси x
        (0, 1, 0), (0, -1, 0),  # движение по оси y
        (0, 0, 1), (0, 0, -1)   # движение по оси z
    ]
    
    # Проверка на валидность клетки
    def is_valid_move(point: Point):
        return (0 <= point.x < x_len and 
                0 <= point.y < y_len and 
                0 <= point.z < z_len and 
                field[point.x][point.y][point.z] >= 1 and 
                point not in [Point(seg.root[0], seg.root[1], seg.root[2]) for seg in snake.geometry])

    # Эвристическая функция для A* (расстояние до цели)
    def heuristic(current: Point, goal: Point):
        return sqrt((goal.x - current.x) ** 2 + (goal.y - current.y) ** 2 + (goal.z - current.z) ** 2)
    
    # Алгоритм A* для поиска пути
    def a_star(start: Point, goal: Point):
        # Очередь с приоритетами (f = g + h)
        open_list = []
        heapq.heappush(open_list, (0 + heuristic(start, goal), 0, (start.x, start.y, start.z), []))  # f, g, координаты точки, путь
        g_costs = { (start.x, start.y, start.z): 0 }  # стоимость пути для каждой точки
        visited = set()
        
        while open_list:
            # Получаем точку с минимальной стоимостью
            _, g, current_point_coords, path = heapq.heappop(open_list)
            current_point = Point(*current_point_coords)  # восстановление объекта Point
            
            # Если мы достигли цели, возвращаем путь
            if current_point == goal:
                return path + [current_point]
            
            # Проверка всех соседей
            for dx, dy, dz in directions:
                neighbor = Point(current_point.x + dx, current_point.y + dy, current_point.z + dz)
                
                if is_valid_move(neighbor) and (neighbor.x, neighbor.y, neighbor.z) not in visited:
                    new_g_cost = g + 1  # Стоимость перехода на соседнюю клетку
                    if (neighbor.x, neighbor.y, neighbor.z) not in g_costs or new_g_cost < g_costs[(neighbor.x, neighbor.y, neighbor.z)]:
                        g_costs[(neighbor.x, neighbor.y, neighbor.z)] = new_g_cost
                        f_cost = new_g_cost + heuristic(neighbor, goal)  # f = g + h
                        heapq.heappush(open_list, (f_cost, new_g_cost, (neighbor.x, neighbor.y, neighbor.z), path + [current_point]))
            
            visited.add((current_point.x, current_point.y, current_point.z))
        
        return []  # Если путь не найден, возвращаем пустой список
    
    # Запуск A* для поиска пути от стартовой точки до цели
    return a_star(start, goal)