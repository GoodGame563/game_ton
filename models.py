from pydantic import BaseModel

class OurSnake(BaseModel):
    id:int
    direction: str
    oldDirection: str
    geometry: list
    deathCount: int
    status: str
    reviveRamainMs: int

class EnemyShake(BaseModel):
    geometry: list 
    status: str
    kills: int

class Food(BaseModel):
    c: list
    points: int

class BaseInfo(BaseModel):
    mapSize: int
    name: str
    points: int
    fences: list
    snakes: list[OurSnake]
    enemies: list[EnemyShake]
    food: list[Food]
    specialFood: list[Food] 
    turn: int
    tickRemainMs: int
    reviveTimeoutSec: int
    errors: list
