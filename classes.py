from dataclasses import dataclass
from models import Food

@dataclass
class Point:
    x: int
    y: int
    z: int

    def to_list(self):
        return [self.x, self.y, self.z]
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

@dataclass
class FoodLength:
    food: Food
    length: int