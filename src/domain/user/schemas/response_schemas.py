from pydantic import Field

from src.core.server.base_response import BaseResponse


class RegistrationResponse(BaseResponse):
    id: int = Field("Индентификатор пользователя")
