from enum import Enum

class B(Enum):
    y: int = 1
    x: int = 2
    z: int = 3

next_movie: B = B.x

def set_next_movie():
    if next_movie == B.x:
        next_movie = B.y
    
    elif next_movie == B.y:
        next_movie = B.z
    
    else:
        next_movie = B.x

def move(body, head, orange, field):
    if next_movie == B.x:
        if head.x < orange.x:
            head.x += 1
        elif head.x > orange.x:
            head.x -= 1
        else:
            if head.y < orange.y:
                head.y += 1
            elif head.y > orange.y:
                head.y -= 1

            elif head.z < orange.z:
                head.z += 1
            elif head.z > orange.z:
                head.z -= 1
    
    if next_movie == B.y:
        if head.y < orange.y:
            head.y += 1
        elif head.y > orange.y:
            head.y -= 1
        else:
            if head.x < orange.x:
                head.x += 1
            elif head.x > orange.x:
                head.x -= 1
            elif head.z < orange.z:
                head.z += 1
            elif head.z > orange.z:
                head.z -= 1
    
    if next_movie == B.z:
        if head.z < orange.z:
            head.z += 1
        elif head.z > orange.z:
            head.z -= 1
        else:
            if head.x < orange.x:
                head.x += 1
            elif head.x > orange.x:
                head.y -= 1
            elif head.y < orange.y:
                head.y += 1
            elif head.y > orange.y:
                head.y -= 1

    set_next_movie()
    
    return head