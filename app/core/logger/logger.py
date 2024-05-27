import sys

from loguru import logger


class Logger:
    def __init__(self):
        self.logger = logger

        self.logger.add(
            sys.stderr,
            colorize=True,
            format="<green>{time} | {level} | {message}</green>",
            filter="my_module",
            level="INFO",
        )
        self.logger.add(
            sys.stderr,
            colorize=True,
            format="<yellow>{time} | {level} | {message}</yellow>",
            filter="my_module",
            level="WARNING",
        )
        self.logger.add(
            sys.stderr,
            colorize=True,
            format="<red>{time} | {level} | {message}</red>",
            filter="my_module",
            level="ERROR",
        )

    def info(self, message: str) -> None:
        self.logger.info(message)

    def warning(self, message: str) -> None:
        self.logger.warning(message)

    def error(self, message: str) -> None:
        self.logger.warning(message)
