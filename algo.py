from dataclasses import dataclass
from collections import deque

import numpy as np

@dataclass
class A:
    x: int
    y: int
    z: int

def find_orange(head, array, body, x_len, y_len, z_len):
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
        
        if x_len > cur.x + 1:
            huy.append(A(cur.x+1, cur.y, cur.z))
        
        if y_len > cur.y + 1:
            huy.append(A(cur.x+1, cur.y, cur.z))
        
        if z_len > cur.z + 1:
            huy.append(A(cur.x+1, cur.y, cur.z))
        
        if cur.x - 1:
            huy.append(A(cur.x+1, cur.y, cur.z))
        
        if cur.y - 1:
            huy.append(A(cur.x+1, cur.y, cur.z))
        
        if cur.z - 1:
            huy.append(A(cur.x+1, cur.y, cur.z))
    
    return result
