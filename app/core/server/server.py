import asyncio

import uvicorn
from fastapi import (
    FastAPI,
    APIRouter
)

from migrations.migrator import Migrator
from interfaces.repo_interfaces import RepositoryInterface


class Server:
    """ Класс отвечающий за работу сервера """

    def __init__(
            self,
            host: str = "0.0.0.0",
            port: int = 8080,
            debug: bool = True,
            version: str = "0.0.1",
            title: str = "App",
            repo: RepositoryInterface = None,
            routers: APIRouter = None
    ):
        self._host = host
        self._port = port
        self._routers = routers
        self._debug = debug
        self._version = version
        self._title = title
        self._repo = repo

        self._app = FastAPI()

    def _configure_server(self):
        """ Метод кофигурации необязательных аргументов
        FastAPI """

        if self._debug:
            self._app.debug = self._debug
        if self._version:
            self._app.version = self._version
        if self._title:
            self._app.title = self._title

    def _add_routers(self):
        """ Метод для инициализации маршрутов """
        if self._routers:
            self._app.include_router(self._routers)

    def add_middleware(self, middleware, **options):
        """ Метод для добавления middlewares """
        self._app.add_middleware(middleware, **options)

    async def make_migration(self):
        """ Метод реализующий запуск миграций """
        migrator = Migrator(repository=self._repo)
        await migrator.make_migration()

    def start_server(self):
        """ Метод отвечающий за запуск сервиса """
        self._configure_server()
        self._add_routers()
        if self._repo:
            asyncio.run(self.make_migration())
        uvicorn.run(
            app=self._app,
            host=self._host,
            port=self._port
        )
