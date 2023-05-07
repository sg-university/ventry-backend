from fastapi import APIRouter

from app.outers.interfaces.deliveries.controllers import location_controller, item_file_map_controller, \
    transaction_controller, transaction_item_map_controller, file_controller, role_controller, \
    inventory_control_controller, item_bundle_map_controller, account_controller, \
    item_controller, forecast_controller, authentication_controller, company_controller

api_v1_router: APIRouter = APIRouter(prefix="/v1", tags=["v1"])
api_v1_router.include_router(role_controller.router)
api_v1_router.include_router(account_controller.router)
api_v1_router.include_router(location_controller.router)
api_v1_router.include_router(company_controller.router)
api_v1_router.include_router(item_controller.router)
api_v1_router.include_router(file_controller.router)
api_v1_router.include_router(item_file_map_controller.router)
api_v1_router.include_router(item_bundle_map_controller.router)
api_v1_router.include_router(inventory_control_controller.router)
api_v1_router.include_router(transaction_controller.router)
api_v1_router.include_router(transaction_item_map_controller.router)
api_v1_router.include_router(forecast_controller.router)
api_v1_router.include_router(authentication_controller.router)
