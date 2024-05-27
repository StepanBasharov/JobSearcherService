from time import time

from src.core.server.base_response import BaseResponse


class ServerTools:
    @staticmethod
    def request_time(func):
        async def wrapper(*args, **kwargs):
            start = time()
            result: BaseResponse = await func(*args, **kwargs)
            end = time()
            result.time = end - start
            return result

        return wrapper
