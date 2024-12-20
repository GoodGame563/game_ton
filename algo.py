from classes import Point
from collections import deque
from models import GameState, Snake
import numpy as np 


def find_orange(snake: Snake, array: np.ndarray, x_len:int, y_len:int, z_len:int) -> Point:
    first_element = snake.geometry[1]
    head = Point(first_element.root[0], first_element.root[1], first_element.root[2])
    body = []
    for i in snake.geometry[1:]:
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
            huy.append(Point(cur.x+1, cur.y, cur.z))
        
        if z_len - 1 > cur.z + 1:
            huy.append(Point(cur.x+1, cur.y, cur.z))
        
        if cur.x - 1 < 0:
            huy.append(Point(cur.x+1, cur.y, cur.z))
        
        if cur.y - 1 < 0:
            huy.append(Point(cur.x+1, cur.y, cur.z))
        
        if cur.z - 1 < 0:
            huy.append(Point(cur.x+1, cur.y, cur.z))

        visited.append(cur)
    
    return result
