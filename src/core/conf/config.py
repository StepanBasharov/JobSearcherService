import yaml

from pydantic import BaseModel

from src.core.constants import CONFIG_PATH


class ServerConfig(BaseModel):
    host: str
    port: int
    debug: bool | None
    version: str | None
    title: str | None


class DataBaseConfig(BaseModel):
    host: str
    port: int
    db: str
    user: str
    password: str


class Config(BaseModel):
    server: ServerConfig
    database: DataBaseConfig

    @classmethod
    def new_config(cls):
        """Инициализация нового конфига из yaml"""
        with open(CONFIG_PATH, "r") as config_file:
            config = yaml.safe_load(config_file)
            return cls(**config)

    @property
    def get_server_conf(self):
        """Получение конфигурации сервера"""
        return (
            self.server.host,
            self.server.port,
            self.server.debug,
            self.server.version,
            self.server.title,
        )

    @property
    def get_database_conf(self):
        """Получение конфигурации бд"""
        return (
            self.database.host,
            self.database.port,
            self.database.db,
            self.database.user,
            self.database.password,
        )
