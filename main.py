from api_connect import get_map, move_snakes
from field import return_fields
from algo import find_orange, new_algo_find, find_nearest_safe_food, new_algo_find_v2
from move import move, find_path, find_optimal_path
from models import SnakeRequest, SnakeSmall, Direction3D, GameState, Snake
from classes import Point
import json
import time
import numpy as np


# def get_neighbors_around_point(snake: Snake, array: np.ndarray, radius: int) -> list[Point]:
#     elements = snake.geometry.copy()
#     elements.reverse()
#     first_element = elements.pop()
#     center = Point(first_element.root[0], first_element.root[1], first_element.root[2])
#     # Список для хранения найденных точек
#     neighbors = []
    
#     # Перебираем все точки в области вокруг центра в пределах радиуса
#     for dx in range(-radius, radius + 1):
#         for dy in range(-radius, radius + 1):
#             for dz in range(-radius, radius + 1):
#                 nx, ny, nz = center.x + dx, center.y + dy, center.z + dz
                
#                 # Проверяем, чтобы координаты были внутри массива
#                 if (0 <= nx < array.shape[0] and 0 <= ny < array.shape[1] and 0 <= nz < array.shape[2]):
#                     # Проверяем, если значение больше 1
#                     if array[nx, ny, nz] > 1:
#                         neighbors.append(Point(nx, ny, nz))
    
#     return neighbors

# with open('data.json') as file:
#     gs = GameState(**json.load(file))
# array = return_fields(gs)
# go_to_snakes = []
# for snake in gs.snakes:
#     print(get_neighbors_around_point(snake, array,100))
    # my_orage = new_algo_find(snake, gs.food)
    # orage_cord = Point(my_orage.food.c.root[0], my_orage.food.c.root[1],my_orage.food.c.root[2])
    # print(f"goal {orage_cord}" )
    # go_to = find_path(snake, orage_cord, array, gs.mapSize[0], gs.mapSize[1], gs.mapSize[2])
    # print(len(go_to))  
    # go_to = find_optimal_path(snake, orage_cord, array, gs.mapSize[0], gs.mapSize[1], gs.mapSize[2])
    # print(len(go_to))  


while True:
    gs = get_map()
    if gs == None: 
        print("Жду запуск")
        time.sleep(5)
        continue
    # with open('data.json') as file:
    #     gs = GameState(**json.load(file))
    for food in gs.food:
        if food.type != 0:
            print(f"{food}")
    array = return_fields(gs)
    go_to_snakes = []
    snake_num = 1
    for snake in gs.snakes:     
        print(f"snake number {snake_num} id snake {snake.id} snake status {snake.status} snake length {len (snake.geometry)}")
        if snake.status == "alive":
            array = return_fields(gs)
            new_go = new_algo_find_v2(snake, gs.food, gs.enemies)
            orage_cord = Point(new_go.food.c.root[0], new_go.food.c.root[1],new_go.food.c.root[2])
            go_to = move(snake, orage_cord, array, gs.mapSize[0], gs.mapSize[1], gs.mapSize[2])
            direction = Direction3D(go_to.to_list())
            gs = move_snakes(SnakeRequest(snakes=[SnakeSmall(id = snake.id, direction = direction)]))
            
        #     new_go = find_nearest_safe_food(snake, array, gs.mapSize[0], gs.mapSize[1], gs.mapSize[2], gs.food)
        #     go_to = move(snake, new_go, array, gs.mapSize[0], gs.mapSize[1], gs.mapSize[2])
        #     direction = Direction3D(go_to.to_list())
        #     gs = move_snakes(SnakeRequest(snakes=[SnakeSmall(id = snake.id, direction = direction)]))
        # # if snake_num == 0:
        #     if snake.status == "alive":
        #         my_orage = new_algo_find(snake, gs.food)
        #         orage_cord = Point(my_orage.food.c.root[0], my_orage.food.c.root[1],my_orage.food.c.root[2])
        #         go_to = move(snake, orage_cord, array, gs.mapSize[0], gs.mapSize[1], gs.mapSize[2])
        #         direction = Direction3D(go_to.to_list())
        #         new_gs = move_snakes(SnakeRequest(snakes=[SnakeSmall(id = snake.id, direction = direction)]))
        #     snake_num = 1
        # elif snake_num == 1:
           
        #     snake_num = 2
        # else: 
        #     if snake.status == "alive":
        #         new_go = new_algo_find_v2(snake, gs.food, gs.enemies)
        #         orage_cord = Point(new_go.food.c.root[0], new_go.food.c.root[1],new_go.food.c.root[2])
        #         go_to = move(snake, orage_cord, array, gs.mapSize[0], gs.mapSize[1], gs.mapSize[2])
        #         direction = Direction3D(go_to.to_list())
        #         new_gs = move_snakes(SnakeRequest(snakes=[SnakeSmall(id = snake.id, direction = direction)]))
        #     snake_number = 1

        # if new_gs.errors != []:
        #     print(new_gs.errors)
        # if snake.status == "alive":
        #     my_orage = new_algo_find(snake, gs.food)
        #     print(my_orage)
        #     new_go = find_nearest_safe_food(snake, array, gs.mapSize[0], gs.mapSize[1], gs.mapSize[2], gs.food)
        #     print(new_go)
        #     # orage_cord = Point(my_orage.food.c.root[0], my_orage.food.c.root[1],my_orage.food.c.root[2])
        #     go_to = move(snake, new_go, array, gs.mapSize[0], gs.mapSize[1], gs.mapSize[2])
        #     direction = Direction3D(go_to.to_list())
        #     print(go_to)
        #     # go_to_snakes.append(SnakeSmall(id = snake.id, direction = direction))

            # new_gs = move_snakes(SnakeRequest(snakes=[SnakeSmall(id = snake.id, direction = direction)]))
            # if new_gs.errors != []:
            #     print(new_gs.errors)