from fastapi import APIRouter

from src.domain.user.api.v1 import user_api_v1


api = APIRouter(prefix="/api")
api.include_router(user_api_v1)
