from fastapi import FastAPI
from api.stores import router as stores_router
from api.inventory import router as inventory_router

app = FastAPI(title="Store Operations Service")

app.include_router(stores_router)
app.include_router(inventory_router)

@app.get("/")
def home():
    return {"message": "Store Operations Service is running"}
