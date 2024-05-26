from fastapi import APIRouter

from app.domain.user.schemas.request_schemas import RegistrationRequest
from app.domain.user.schemas.response_schemas import RegistrationResponse

user_api_v1 = APIRouter(prefix="/v1/user", tags=["Users V1"])


@user_api_v1.post("/registration")
async def registration(request: RegistrationRequest) -> RegistrationResponse:
    ...
