from pydantic import BaseModel, Field


class BaseResponse(BaseModel):
    result: bool = Field("Результат запроса")
    time: int = Field("Время выполнения запроса")


class ErrorResponse(BaseResponse):
    message: str = Field("Сообщение об ошибке")
