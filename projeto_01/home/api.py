from ninja import NinjaAPI
from app1.api.app1 import router as app1_router

api = NinjaAPI()
api.add_router("/app1/", app1_router)