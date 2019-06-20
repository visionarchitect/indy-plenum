from abc import ABC, abstractmethod
from random import Random
from typing import Any


class SimRandom(ABC):
    @abstractmethod
    def integer(self, min: int, max: int) -> int:
        pass

    @abstractmethod
    def choice(self, *args) -> Any:
        pass


class DefaultSimRandom(SimRandom):
    # TODO: Consider making seed fixed to make it always deterministic
    def __init__(self, seed=None):
        self._random = Random(seed)

    def integer(self, min: int, max: int) -> int:
        return self._random.randint(min, max)

    def choice(self, *args) -> Any:
        return self._random.choice(args)
