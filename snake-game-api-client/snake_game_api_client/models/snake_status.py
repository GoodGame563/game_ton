from enum import Enum


class SnakeStatus(str, Enum):
    ALIVE = "alive"
    DEAD = "dead"

    def __str__(self) -> str:
        return str(self.value)
