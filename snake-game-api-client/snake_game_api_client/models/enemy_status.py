from enum import Enum


class EnemyStatus(str, Enum):
    ALIVE = "alive"
    DEAD = "dead"

    def __str__(self) -> str:
        return str(self.value)
