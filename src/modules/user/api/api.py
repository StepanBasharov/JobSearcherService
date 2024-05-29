from fastapi import APIRouter

from src.modules.user.schemas.request_schemas import (
    RegistrationRequest,
    LoginRequest
)
from src.modules.user.schemas.response_schemas import RegistrationResponse
from src.modules.user.use_case.user_registration_use_case import RegistrationUseCase
from src.modules.user.use_case.user_login_use_case import LoginUseCase

user_api = APIRouter(prefix="/user", tags=["Users"])


@user_api.post("/registration")
async def registration(request: RegistrationRequest) -> RegistrationResponse:
    use_case = RegistrationUseCase(request=request)
    return await use_case.execute()


@user_api.post("/login")
async def login(request: LoginRequest):
    use_case = LoginUseCase(request=request)
    return await use_case.execute()
