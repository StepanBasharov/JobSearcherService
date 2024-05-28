import asyncio

from src.infrastructure.server.server import Server
from src.infrastructure.database.database import Database
from src.core.conf.config import Config
from src.infrastructure.logger.logger import Logger
from src.infrastructure.api import api
from migrations.migrator import Migrator

if __name__ == "__main__":
    logger = Logger()

    config = Config.new_config()
    logger.info("INIT CONFIG")

    db = Database(*config.get_database_conf)
    logger.info("INIT DATABASE")

    asyncio.run(Migrator(db=db).make_migration())
    logger.info("MAKE MIGRATIONS")

    server = Server(*config.get_server_conf, routers=api)
    logger.info("CONFIGURE SERVER")
    server.start_server()
