import numpy as np
from models import GameState, Point3D, Snake, Food, Enemy
import json
array = np.array((1, 1, 1), dtype=np.int32)

def create_field(map_size_x, map_size_y, map_size_z):
    global array
    array = np.ones((map_size_x, map_size_y, map_size_z), dtype=np.int32)

def poke_anything(list_cord: Point3D, value: int):
    global array
    try:
        array[list_cord.root[0]][list_cord.root[1]][list_cord.root[2]] = np.int32(value)
    except IndexError:
        print("Index out of range")

def poke_all_oranges(oranges: list[Food]):
    for orange in oranges:
        poke_anything(orange.c, orange.points)

def poke_my_snakes(snakes: list[Snake]):
    for snake in snakes:
        for snake_g in snake.geometry:
            poke_anything(snake_g, -1)

def poke_enemy_snakes(snakes: list[Enemy]):
    for snake in snakes:
        if snake.status == "alive":
            for snake_g in snake.geometry:
                poke_anything(snake_g, -2)

def poke_all_holes(holes: list[Point3D]):
    for hole in holes:
        poke_anything(hole, 0)

def return_fields(gs: GameState) -> np.ndarray: 
    global array
    create_field(gs.mapSize[0], gs.mapSize[1], gs.mapSize[2])
    poke_all_holes(gs.fences)
    poke_my_snakes(gs.snakes)
    poke_all_oranges(gs.food)
    poke_enemy_snakes(gs.enemies)
    return array

