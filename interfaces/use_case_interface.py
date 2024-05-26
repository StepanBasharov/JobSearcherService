from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class UseCaseInterface(ABC):
    @abstractmethod
    async def execute(self):
        ...
