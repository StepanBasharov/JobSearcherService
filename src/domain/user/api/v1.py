from fastapi import APIRouter

from src.domain.user.schemas.request_schemas import (
    RegistrationRequest,
    LoginRequest
)
from src.domain.user.schemas.response_schemas import RegistrationResponse
from src.domain.user.use_case.user_registration_use_case import RegistrationUseCase
from src.domain.user.use_case.user_login_use_case import LoginUseCase

user_api_v1 = APIRouter(prefix="/v1/user", tags=["Users V1"])


@user_api_v1.post("/registration")
async def registration(request: RegistrationRequest) -> RegistrationResponse:
    use_case = RegistrationUseCase(request=request)
    return await use_case.execute()


@user_api_v1.post("/login")
async def login(request: LoginRequest):
    use_case = LoginUseCase(request=request)
    return await use_case.execute()
