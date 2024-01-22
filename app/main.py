from fastapi import FastAPI
from app.api.routers import router as menu_router

app = FastAPI(title='Restaurant Menu', version='1.0')

app.include_router(menu_router)
