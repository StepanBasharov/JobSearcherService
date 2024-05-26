from app.core.database.database import Database
from app.core.conf.config import Config
from interfaces.repo_interfaces import RepositoryInterface


class Repository(RepositoryInterface):
    """ Класс для инфраструктуроной работы с БД """
    def __init__(
            self,
            config: Config
    ):
        self.db = Database(*config.get_database_conf)

    async def sql_execute(self, sql_raw: str) -> None:
        conn = await self.db.get_connection()
        await conn.execute(sql_raw)
        await conn.close()
