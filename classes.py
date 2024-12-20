from dataclasses import dataclass
from models import Food, SpecialFood

@dataclass
class Point:
    x: int
    y: int
    z: int

    def to_list(self):
        return [self.x, self.y, self.z]
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)
    def __hash__(self):
        return hash((self.x, self.y, self.z))

@dataclass
class FoodLength:
    food: Food | SpecialFood
    length: int