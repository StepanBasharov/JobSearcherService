from fastapi import APIRouter

from src.modules.user.api import user_api

api_v1 = APIRouter(prefix="/v1")

api_v1.include_router(user_api)
