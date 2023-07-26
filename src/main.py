from fastapi import FastAPI
from src.api.routers import routers


app = FastAPI(
    title='t_tracker'
)

for router in routers:
    app.include_router(router)
