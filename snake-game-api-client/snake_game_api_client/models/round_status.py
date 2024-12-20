from enum import Enum


class RoundStatus(str, Enum):
    ACTIVE = "active"
    ENDED = "ended"
    NOT_STARTED = "not started"

    def __str__(self) -> str:
        return str(self.value)
