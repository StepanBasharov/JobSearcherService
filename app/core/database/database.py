import asyncpg


class Database:
    """ Класс конкретной реализации для asyncpg """
    def __init__(
            self,
            host: str = "0.0.0.0",
            port: int = 5432,
            db: str = "postgres",
            user: str = "postgres",
            password: str = "postgres"
    ):
        self.db_host = host
        self.db_port = port
        self.db_name = db
        self.db_user = user
        self.db_password = password

    async def get_connection(self) -> asyncpg.Connection:
        """ Получение подключеняи к бд """
        conn = await asyncpg.connect(
            host=self.db_host,
            port=self.db_port,
            database=self.db_name,
            user=self.db_user,
            password=self.db_password
        )
        return conn
