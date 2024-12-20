from api_connect import get_map
from field import return_fields
from algo import find_orange
from move import move

gs = get_map()
array = return_fields(gs)
for snake in gs.snakes:
    my_orage = find_orange(snake, array, gs.mapSize[0], gs.mapSize[1], gs.mapSize[2])
    go_to = move(snake, my_orage, array, gs.mapSize[0], gs.mapSize[1], gs.mapSize[2])
    print(go_to)