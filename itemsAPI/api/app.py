from fastapi import FastAPI
from api.routes.item_router import router as item_router

app = FastAPI()
app.include_router(item_router, tags=["Items"], prefix="/items")