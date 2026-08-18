from fastapi import FastAPI
from controller.HomeController import router

app = FastAPI()

app.include_router(router)