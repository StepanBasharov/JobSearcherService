from abc import ABC, abstractmethod


class UserRepositoryInterface(ABC):
    @abstractmethod
    async def create_new_user(self, ):