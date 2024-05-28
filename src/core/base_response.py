from pydantic import BaseModel, Field


class BaseResponse(BaseModel):
    result: bool = Field("Результат запроса")


class ErrorResponse(BaseResponse):
    message: str = Field("Сообщение об ошибке")
