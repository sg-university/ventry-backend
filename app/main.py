from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseConfig

from app.outer.interfaces.deliveries.routers.api_router import router

app = FastAPI(
    title="ventry-backend"
)

app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    router=router,
)

BaseConfig.arbitrary_types_allowed = True
