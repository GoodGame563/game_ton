from dataclasses import dataclass
from collections import deque

import numpy as np

@dataclass
class A:
    x: int
    y: int
    z: int

def find_orange(head, array, body):
    huy = deque()
    huy.append(head)
    result = None

    while huy:
        cur = huy.popleft()
        if array[cur.x][cur.y][cur.z] > 1:
            for bod in body:
                if cur.x < bod.x or cur.y < bod.y or cur.z < bod.z:
                    continue
            result = cur
            break
        
        if len(array) > cur.x + 1:
            huy.append(A(cur.x+1, cur.y, cur.z))
        
        if len(array) > cur.y + 1:
            huy.append(A(cur.x+1, cur.y, cur.z))
        
        if len(array) > cur.z + 1:
            huy.append(A(cur.x+1, cur.y, cur.z))
        
        if cur.x - 1:
            huy.append(A(cur.x+1, cur.y, cur.z))
        
        if cur.y - 1:
            huy.append(A(cur.x+1, cur.y, cur.z))
        
        if cur.z - 1:
            huy.append(A(cur.x+1, cur.y, cur.z))
    
    return result
