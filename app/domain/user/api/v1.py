from typing import Union

from fastapi import APIRouter

from app.domain.user.schemas.request_schemas import RegistrationRequest
from app.domain.user.schemas.response_schemas import RegistrationResponse
from app.domain.user.use_case.user_registration_use_case import RegistrationUseCase

user_api_v1 = APIRouter(prefix="/v1/user", tags=["Users V1"])


@user_api_v1.post("/registration")
async def registration(request: RegistrationRequest) -> RegistrationResponse:
    use_case = RegistrationUseCase(request=request)
    return await use_case.execute()
