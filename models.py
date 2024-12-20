from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class Direction3D(BaseModel):
    x: int
    y: int
    z: int

class Point3D(BaseModel):
    x: int
    y: int
    z: int

class SnakeRequestItem(BaseModel):
    id: str
    direction: Direction3D

class SnakeRequest(BaseModel):
    snakes: List[SnakeRequestItem]

class Snake(BaseModel):
    id: str
    direction: Direction3D
    old_direction: Optional[Direction3D]
    geometry: List[Point3D]
    death_count: int
    status: str
    revive_remain_ms: int

class Enemy(BaseModel):
    geometry: List[Point3D]
    status: str
    kills: int

class Food(BaseModel):
    c: Point3D
    points: int

class SpecialFood(BaseModel):
    golden: List[Point3D]
    suspicious: List[Point3D]

class GameState(BaseModel):
    map_size: List[int]
    name: str
    points: int
    fences: List[Point3D]
    snakes: List[Snake]
    enemies: List[Enemy]
    food: List[Food]
    special_food: SpecialFood
    turn: int
    revive_timeout_sec: int
    tick_remain_ms: int
    errors: Optional[List[str]]

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
