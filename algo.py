from math import sqrt, floor
from typing import List

from classes import Point, FoodLength
from models import  Snake, Food, Enemy


def new_algo_find(snake: Snake, foods: List[Food], enemies: List[Enemy]) -> FoodLength:
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

        distance = _calculate_distance(x1=x, y1=y, z1=z, x2=head.x, y2=head.y, z2=head.z)

        result.append(FoodLength(food=food, length=floor(distance)))

    return _custom_min(result, enemies)

def _calculate_distance(x1, y1, z1, x2, y2, z2) -> float:
    return sqrt(
        (x1 - x2) ** 2 +
        (y1 - y2) ** 2 +
        (z1 - z2) ** 2
    )

def _custom_min(elems: List[FoodLength], enemies: List[Enemy]) -> FoodLength:
    result = elems[0]
    min_enemy_to_fruit = min(map(lambda x: _calculate_distance(result.food.c.root[0], result.food.c.root[1], result.food.c.root[2], x.geometry[0].root[0], x.geometry[0].root[1], x.geometry[0].root[2]), enemies))

    for i in range(1, len(elems)):
        cur_enemy_to_fruit = min(map(lambda x: _calculate_distance(elems[i].food.c.root[0], elems[i].food.c.root[1], elems[i].food.c.root[2], x.geometry[0].root[0], x.geometry[0].root[1], x.geometry[0].root[2]), enemies))
        
        if result.length > elems[i].length and min_enemy_to_fruit > cur_enemy_to_fruit:
            result = elems[i]
            min_enemy_to_fruit = cur_enemy_to_fruit

    return result
