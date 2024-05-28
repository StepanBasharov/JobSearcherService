from abc import ABC, abstractmethod


class UseCaseInterface(ABC):
    @abstractmethod
    async def execute(self): ...
