from abc import ABC, abstractmethod


class UserRepositoryInterface(ABC):
    @abstractmethod
    async def create_new_user(
        self,
        first_name,
        last_name,
        patronymic,
        age,
        email,
        phone,
        password,
        date_of_birth,
        living,
    ): ...

    @abstractmethod
    async def get_user_by_email(self, email): ...
