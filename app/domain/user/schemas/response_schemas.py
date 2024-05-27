from pydantic import Field

from app.core.server.base_response import BaseResponse


class RegistrationResponse(BaseResponse):
    id: int = Field("Индентификатор пользователя")
