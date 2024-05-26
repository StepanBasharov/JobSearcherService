from abc import ABC, abstractmethod


class RepositoryInterface(ABC):
    @abstractmethod
    async def sql_execute(self, sql_raw) -> None:
        ...
