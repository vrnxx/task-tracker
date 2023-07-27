import uvicorn
from fastapi import FastAPI

from src.api.routers import routers

app = FastAPI(
    title='t_tracker',
    version='0.1.1'
)

for router in routers:
    app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8000, reload=True)
