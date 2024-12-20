from classes import Point, FoodLength
from collections import deque
from models import GameState, Snake, Food
import numpy as np 
from math import sqrt


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