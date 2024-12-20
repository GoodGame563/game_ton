import numpy as np

def create_field(map_size):
    return np.ones((map_size, map_size, map_size), dtype=np.int8)

def poke_all_oranges(array, oranges):
    for orange in oranges:
        poke_orange(array, orange.x, orange.y, orange.z)

def poke_orange(array, x, y, z, value):
    array[x][y][z] = value

def poke_my_snake(array, snakes):
    for snake in snakes:
        poke_snake(array, snake.x, snake.y, snake.z)

def poke_snake(array, x, y, z):
    array[x][y][z] = -1

def poke_all_holes(array, holes):
    for hole in holes:
        poke_holes(array, hole.x, hole.y, hole.z)

def poke_holes(array, x: int, y: int, z: int):
    array[x][y][z] = np.int8(0)

if __name__ == "__main__":
    result = create_field(10)
    print(result)
    poke_holes(result, 0, 0, 0)
    print("poke first")
    print(result)
    poke_holes(result, 1, 1, 1)
    print("poke second")
    print(result)

    class A:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

    poke_all_holes(result, [A(1, 2, 3), A(2, 2, 2), A(3, 5, 5)])
    print("poke all")
    print(result)
