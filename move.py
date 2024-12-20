from enum import Enum
from classes import Point
from models import Snake
import numpy as np
from math import sqrt

def move(snake: Snake, orange: Point, field: np.ndarray, x_len:int, y_len:int, z_len:int) -> Point:
    first_element = snake.geometry.pop()
    head = Point(first_element[0], first_element[1], first_element[2])
    body = []
    for i in snake.geometry:
        body.append(Point(i[0], i[1], i[2]))

    result = Point(head.x, head.y, head.z)

    def is_valid_move(next_point: Point):
        return (
            0 <= next_point.x < x_len and
            0 <= next_point.y < y_len and
            0 <= next_point.z < z_len and
            field[next_point.x][next_point.y][next_point.z] != 0 and
            _check_body(body, next_point)
        )

    def distance_to_goal(point: Point):
        return sqrt(
            (orange.x - point.x) ** 2 +
            (orange.y - point.y) ** 2 +
            (orange.z - point.z) ** 2
        )

    neighbors = [
        Point(head.x + 1, head.y, head.z),
        Point(head.x - 1, head.y, head.z),
        Point(head.x, head.y + 1, head.z),
        Point(head.x, head.y - 1, head.z),
        Point(head.x, head.y, head.z + 1),
        Point(head.x, head.y, head.z - 1),
    ]

    valid_neighbors = [p for p in neighbors if is_valid_move(p)]

    if valid_neighbors:
        result = min(valid_neighbors, key=distance_to_goal)
    else:
        result = head

    return result


def _check_body(body, next_point):
    return next_point not in body
