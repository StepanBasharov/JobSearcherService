import asyncio

from src.core.server.server import Server
from src.core.database.database import Database
from src.core.conf.config import Config
from src.core.logger.logger import Logger
from src.domain import api
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
