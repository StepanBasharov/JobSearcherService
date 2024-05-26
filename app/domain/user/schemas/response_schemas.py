from pydantic import BaseModel, Field


class BaseResponse(BaseModel):
    result: bool = Field("Результат запроса")
    time: int = Field("Время выполнения запроса")


class RegistrationResponse(BaseResponse):
    id: int = Field("Индентификатор пользователя")
