from enum import Enum
from dataclasses import dataclass

class B(Enum):
    y: int = 1
    x: int = 2
    z: int = 3

@dataclass
class Point:
    x: int
    y: int
    z: int

next_movie: B = B.x

def set_next_movie():
    if next_movie == B.x:
        next_movie = B.y
    
    elif next_movie == B.y:
        next_movie = B.z
    
    else:
        next_movie = B.x

def move(body, head, orange, field):
    result = Point(head.x, head.y, head.z)
    if next_movie == B.x:
        if head.x < orange.x and check_body(body=body, next_point=Point(head.x+1, head.y, head.z)):
            result.x += 1
        elif head.x > orange.x and check_body(body=body, next_point=Point(head.x-1, head.y, head.z)):
            result.x -= 1
        else:
            if head.y < orange.y and check_body(body=body, next_point=Point(head.x, head.y+1, head.z)):
                result.y += 1
            elif head.y > orange.y and check_body(body=body, next_point=Point(head.x, head.y-1, head.z)):
                result.y -= 1

            elif head.z < orange.z and check_body(body=body, next_point=Point(head.x, head.y, head.z+1)):
                result.z += 1
            elif head.z > orange.z and check_body(body=body, next_point=Point(head.x, head.y, head.z-1)):
                result.z -= 1
    
    if next_movie == B.y:
        if head.y < orange.y and check_body(body=body, next_point=Point(head.x, head.y+1, head.z)):
            result.y += 1
        elif head.y > orange.y and check_body(body=body, next_point=Point(head.x, head.y-1, head.z)):
            result.y -= 1
        else:
            if head.x < orange.x and check_body(body=body, next_point=Point(head.x+1, head.y, head.z)):
                result.x += 1
            elif head.x > orange.x and check_body(body=body, next_point=Point(head.x-1, head.y, head.z)):
                result.x -= 1
            elif head.z < orange.z and check_body(body=body, next_point=Point(head.x, head.y, head.z+1)):
                result.z += 1
            elif head.z > orange.z and check_body(body=body, next_point=Point(head.x, head.y, head.z-1)):
                result.z -= 1
    
    if next_movie == B.z:
        if head.z < orange.z and check_body(body=body, next_point=Point(head.x, head.y, head.z+1)):
            result.z += 1
        elif head.z > orange.z and check_body(body=body, next_point=Point(head.x, head.y, head.z-1)):
            result.z -= 1
        else:
            if head.x < orange.x and check_body(body=body, next_point=Point(head.x+1, head.y, head.z)):
                result.x += 1
            elif head.x > orange.x and check_body(body=body, next_point=Point(head.x-1, head.y, head.z)):
                result.x -= 1
            if head.y < orange.y and check_body(body=body, next_point=Point(head.x, head.y+1, head.z)):
                result.y += 1
            elif head.y > orange.y and check_body(body=body, next_point=Point(head.x, head.y-1, head.z)):
                result.y -= 1

    set_next_movie()
    
    return result

def check_body(body, next_point):
    for bod in body:
        if next_point.x == bod.x and next_point.z == bod.z and next_point.y == bod.y:
            return False

    return True
