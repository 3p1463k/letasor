from fastapi import APIRouter
from apis.version1 import route_home

api_router = APIRouter()

api_router.include_router(route_home.home_router, prefix="", tags=["general_pages"])
