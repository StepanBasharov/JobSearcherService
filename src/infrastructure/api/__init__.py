from fastapi import APIRouter

from src.infrastructure.api.v1 import api_v1

api = APIRouter(prefix="/api")

api.include_router(api_v1)
