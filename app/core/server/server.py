import uvicorn
from fastapi import (
    FastAPI,
    APIRouter,
    Request,
)
from fastapi.responses import JSONResponse

from app.core.base_error import BaseError
from app.core.server.base_response import ErrorResponse


class Server:
    """Класс отвечающий за работу сервера"""

    def __init__(
        self,
        host: str = "0.0.0.0",
        port: int = 8080,
        debug: bool = True,
        version: str = "0.0.1",
        title: str = "App",
        routers: APIRouter = None,
    ):
        self._host = host
        self._port = port
        self._routers = routers
        self._debug = debug
        self._version = version
        self._title = title

        self._app = FastAPI()

        @self._app.exception_handler(BaseError)
        def exception_handler(request: Request, exc: BaseError):
            return JSONResponse(
                status_code=exc.status_code,
                content=ErrorResponse(message=exc.message, result=False, time=1).dict(),
            )

    def _configure_server(self):
        """Метод кофигурации необязательных аргументов
        FastAPI"""

        if self._debug:
            self._app.debug = self._debug
        if self._version:
            self._app.version = self._version
        if self._title:
            self._app.title = self._title

    def _add_routers(self):
        """Метод для инициализации маршрутов"""
        if self._routers:
            self._app.include_router(self._routers)

    def add_middleware(self, middleware, **options):
        """Метод для добавления middlewares"""
        self._app.add_middleware(middleware, **options)

    def start_server(self):
        """Метод отвечающий за запуск сервиса"""
        self._configure_server()
        self._add_routers()
        uvicorn.run(app=self._app, host=self._host, port=self._port)
