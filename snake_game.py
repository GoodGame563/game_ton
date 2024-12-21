import numpy as np
from typing import List
from abc import ABC, abstractmethod


from models import Snake, Food, SnakeSmall
from classes import Point
from move import find_optimal_path
from algo import find_nearest_safe_food, find_max_orange

class SnakeGame(ABC):
    def __init__(self, snake: Snake):
        self._snake_id: str = snake.id
        self._current_food: Point | None = None
        self._current_path: List[Point] | None = None
        self._next_path_idx: int = 0
        self._snake: Snake = snake
        self._field: np.ndarray | None = None

    def is_id(self, snake_id: str) -> bool:
        return self._snake_id == snake_id

    def set_field(self, field: np.ndarray) -> None:
        self._field = field.copy()
    
    def set_snake(self, snake: Snake) -> None:
        if snake.id != self._snake_id:
            raise Exception("Invalid snake")
        
        self._snake = snake

    def reset(self) -> None:
        self._current_food = None
        self._current_path = None
        self._next_path_idx = 0
        self._field = None

    def do_move(self, food: List[Food], x_len = 0, y_len= 0, z_len = 0) -> SnakeSmall:
        if self._field is None :
            raise Exception("field is none")

        if self._current_food is None or self._field[self._current_food.x][self._current_food.y][self._current_food.z] < 2:
            self._current_food = self._find_new_food(
                snake=self._snake, 
                field=self._field, 
                x_len=x_len, 
                y_len=y_len, 
                z_len=z_len, 
                foods=food
                )
            
            self._current_path = find_optimal_path(self._snake, self._current_food, self._field, x_len, y_len, z_len)

        if self._current_path is None:
            self._current_path = find_optimal_path(self._snake, self._current_food, self._field, x_len, y_len, z_len)

        next_point = self._current_path[self._next_path_idx]

        if self._field[next_point.x][next_point.y][next_point.z] < 1:
            self._current_path = find_optimal_path(self._snake, self._current_food, self._field, x_len, y_len, z_len)
            self._next_path_idx = 0
            next_point = self._current_path[self._next_path_idx]

        self._next_path_idx += 1

        head = self._snake.geometry[0]
        head_point = Point(head.root[0], head.root[1], head.root[2])
        next_dir = head_point - next_point

        return SnakeSmall(id=self._snake_id, direction=next_dir)
    
    @abstractmethod
    def _find_new_food(self, snake: Snake, field: np.ndarray, x_len: int, y_len: int, z_len: int, foods: List[Food]) -> Point:
        pass


class SnakeGameFastest(SnakeGame):
    def _find_new_food(self, snake: Snake, field: np.ndarray, x_len: int, y_len: int, z_len: int, foods: List[Food]) -> Point:
        return find_nearest_safe_food(snake, field, x_len, y_len, z_len, foods)


class SnakeGameBiggest(SnakeGame):
    def _find_new_food(self, snake: Snake, field: np.ndarray, x_len: int, y_len: int, z_len: int, foods: List[Food]) -> Point:
        return find_max_orange(snake, foods)