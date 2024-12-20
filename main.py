from api_connect import get_map, move_snakes
from field import return_fields
from algo import find_orange, new_algo_find
from move import move
from models import SnakeRequest, SnakeSmall, Direction3D
from classes import Point
import json
import time

while True:
    gs = get_map()
    if gs == None: 
        print("Жду запуск")
        time.sleep(1)
        continue
    # with open('data.json') as file:
    #     gs = GameState(**json.load(file))
    for snake in  gs.snakes:
        print(snake.status)
        print(snake.geometry)
    array = return_fields(gs)
    go_to_snakes = []
    for snake in gs.snakes:
        my_orage = new_algo_find(snake, gs.food)
        orage_cord = Point(my_orage.food.c.root[0], my_orage.food.c.root[1],my_orage.food.c.root[2])
        go_to = move(snake, orage_cord, array, gs.mapSize[0], gs.mapSize[1], gs.mapSize[2])
        print(go_to)
        direction = Direction3D(go_to.to_list())
        # go_to_snakes.append(SnakeSmall(id = snake.id, direction = direction))

        print(move_snakes(SnakeRequest(snakes=[SnakeSmall(id = snake.id, direction = direction)])))