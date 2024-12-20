from api_connect import get_map, move_snakes
from field import return_fields
from algo import find_orange, new_algo_find
from move import move, find_path, find_optimal_path
from models import SnakeRequest, SnakeSmall, Direction3D, GameState, Snake
from classes import Point
import json
import time
import numpy as np


def get_neighbors_around_point(snake: Snake, array: np.ndarray, radius: int) -> list[Point]:
    elements = snake.geometry.copy()
    elements.reverse()
    first_element = elements.pop()
    center = Point(first_element.root[0], first_element.root[1], first_element.root[2])
    # Список для хранения найденных точек
    neighbors = []
    
    # Перебираем все точки в области вокруг центра в пределах радиуса
    for dx in range(-radius, radius + 1):
        for dy in range(-radius, radius + 1):
            for dz in range(-radius, radius + 1):
                nx, ny, nz = center.x + dx, center.y + dy, center.z + dz
                
                # Проверяем, чтобы координаты были внутри массива
                if (0 <= nx < array.shape[0] and 0 <= ny < array.shape[1] and 0 <= nz < array.shape[2]):
                    # Проверяем, если значение больше 1
                    if array[nx, ny, nz] > 1:
                        neighbors.append(Point(nx, ny, nz))
    
    return neighbors

with open('data.json') as file:
    gs = GameState(**json.load(file))
array = return_fields(gs)
go_to_snakes = []
for snake in gs.snakes:
    print(get_neighbors_around_point(snake, array,100))
    # my_orage = new_algo_find(snake, gs.food)
    # orage_cord = Point(my_orage.food.c.root[0], my_orage.food.c.root[1],my_orage.food.c.root[2])
    # print(f"goal {orage_cord}" )
    # go_to = find_path(snake, orage_cord, array, gs.mapSize[0], gs.mapSize[1], gs.mapSize[2])
    # print(len(go_to))  
    # go_to = find_optimal_path(snake, orage_cord, array, gs.mapSize[0], gs.mapSize[1], gs.mapSize[2])
    # print(len(go_to))  


# while True:
#     gs = get_map()
#     if gs == None: 
#         print("Жду запуск")
#         time.sleep(1)
#         continue
#     # with open('data.json') as file:
#     #     gs = GameState(**json.load(file))
#     for snake in  gs.snakes:
#         print(snake.status)
#         print(snake.geometry)
#     array = return_fields(gs)
#     go_to_snakes = []
#     for snake in gs.snakes:
#         my_orage = new_algo_find(snake, gs.food)
#         orage_cord = Point(my_orage.food.c.root[0], my_orage.food.c.root[1],my_orage.food.c.root[2])
#         go_to = move(snake, orage_cord, array, gs.mapSize[0], gs.mapSize[1], gs.mapSize[2])
#         print(go_to)
#         direction = Direction3D(go_to.to_list())
#         # go_to_snakes.append(SnakeSmall(id = snake.id, direction = direction))

#         print(move_snakes(SnakeRequest(snakes=[SnakeSmall(id = snake.id, direction = direction)])))