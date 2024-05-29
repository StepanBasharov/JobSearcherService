from pydantic import Field

from src.core.base_response import BaseResponse


class RegistrationResponse(BaseResponse):
    id: int = Field("Индентификатор пользователя")


class TokenResponse(BaseResponse):
    token: str
