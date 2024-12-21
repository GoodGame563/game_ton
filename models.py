from typing import List, Optional, Literal
from pydantic import BaseModel, RootModel
from datetime import datetime


class Direction3D(RootModel):
    root: List[int] 

class Point3D(RootModel):
    root: List[int]  

class SnakeSmall(BaseModel):
    id: str
    direction: Direction3D

class SnakeRequest(BaseModel):
    snakes: List[SnakeSmall]

class Snake(BaseModel):
    id: str
    direction: List[int]  
    oldDirection: List[int]  
    geometry: List[Point3D]
    deathCount: int
    status: Literal["alive", "dead"]
    reviveRemainMs: int

class Enemy(BaseModel):
    geometry: List[Point3D]
    status: Literal["alive", "dead"]
    kills: int

class Food(BaseModel):
    c: Point3D
    points: int
    type: Optional[int]  # Добавлен атрибут type

class SpecialFood(BaseModel):
    golden: List[Point3D]
    suspicious: List[Point3D]

class GameState(BaseModel):
    mapSize: List[int]  # [width, height, depth]
    name: str
    points: int
    fences: List[Point3D]
    snakes: List[Snake]
    enemies: List[Enemy]
    food: List[Food]
    specialFood: Optional[SpecialFood]
    turn: int
    reviveTimeoutSec: int
    tickRemainMs: int
    errors: List[str]

class Round(BaseModel):
    name: str
    start_at: datetime
    end_at: datetime
    duration: int
    status: str
    repeat: int

class GameRoundsResponse(BaseModel):
    game_name: str
    rounds: List[Round]
    now: datetime
