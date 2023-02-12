from fastapi import APIRouter

from app.outer.interfaces.deliveries.controllers import role_controller, account_controller, permission_controller, \
    account_permission_map_controller, item_controller

api_v1_router = APIRouter(prefix="/v1", tags=["v1"])
api_v1_router.include_router(role_controller.router)
api_v1_router.include_router(account_controller.router)
api_v1_router.include_router(permission_controller.router)
api_v1_router.include_router(account_permission_map_controller.router)
api_v1_router.include_router(item_controller.router)
