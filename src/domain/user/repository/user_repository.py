from asyncpg import UniqueViolationError

from src.core.database.database import Database
from src.core.conf.config import Config
from src.domain.user.interfaces.repository_interfaces import UserRepositoryInterface
from src.domain.user.repository.models import UserModel
from src.domain.user.errors.database_error import (
    AlreadyExistsError,
    UserNotFoundError
)


class UserRepository(UserRepositoryInterface):
    def __init__(self):
        conf = Config.new_config()
        self.db = Database(*conf.get_database_conf)

    async def create_new_user(
        self,
        first_name,
        last_name,
        age,
        email,
        phone,
        password,
        date_of_birth=None,
        living=None,
        patronymic=None,
    ):
        conn = await self.db.get_connection()
        try:
            await conn.execute(
                """ 
                INSERT INTO job_searcher.users(
                    firstName, 
                    lastName, 
                    patronymic, 
                    age, 
                    email, 
                    phone, 
                    password, 
                    dateOfBirth, 
                    living
                ) VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9)
                """,
                first_name,
                last_name,
                patronymic,
                age,
                email,
                phone,
                password,
                date_of_birth,
                living,
            )
        except UniqueViolationError:
            raise AlreadyExistsError
        await conn.close()

    async def get_user_by_email(self, email) -> UserModel:
        conn = await self.db.get_connection()
        row = await conn.fetchrow(
            "SELECT * FROM job_searcher.users WHERE email = $1", email
        )
        if row:
            return UserModel(**row)
        else:
            raise UserNotFoundError

    async def get_user_by_email_or_phone(self, login: str) -> UserModel:
        conn = await self.db.get_connection()
        row = await conn.fetchrow(
            "SELECT * FROM job_searcher.users WHERE email = $1 OR phone = $1",
            login
        )
        if row:
            return UserModel(**row)
        else:
            raise UserNotFoundError



