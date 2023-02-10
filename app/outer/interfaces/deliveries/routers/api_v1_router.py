from fastapi import APIRouter

from app.outer.interfaces.deliveries.controllers import role_controller


class ApiV1Router:
    def __init__(self, **kwargs: any):
        super().__init__(**kwargs)
        self.router = APIRouter(prefix="/v1", tags=["v1"])
        self.router.include_router(role_controller.router)


api_v1_router = ApiV1Router()
