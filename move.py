from enum import Enum
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    z: int


from math import sqrt

def move(body, head, orange, field, x_len, y_len, z_len):
    result = Point(head.x, head.y, head.z)

    def is_valid_move(next_point):
        return (
            0 <= next_point.x < x_len and
            0 <= next_point.y < y_len and
            0 <= next_point.z < z_len and
            field[next_point.x][next_point.y][next_point.z] != 0 and
            _check_body(body, next_point)
        )

    def distance_to_goal(point):
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
