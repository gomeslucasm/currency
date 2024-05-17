from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.apis.conversion import router as conversion_router

app = FastAPI()

app.include_router(conversion_router, prefix="/api")


@app.get("/")
def docs():
    return RedirectResponse("/docs")
