import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.api.routers import routers
from src.utils.exceptions import StatusNotFoundError, TaskNotFoundError

app = FastAPI(
    title='t_tracker',
    version='0.1.1'
)

for router in routers:
    app.include_router(router)


@app.exception_handler(StatusNotFoundError)
async def status_not_found_handler(request: Request, exc: StatusNotFoundError):
    return JSONResponse(status_code=404, content={'detail': exc.message})


@app.exception_handler(TaskNotFoundError)
async def task_not_found_handler(request: Request, exc: TaskNotFoundError):
    return JSONResponse(status_code=404, content={'detail': exc.message})

if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8000, reload=True)
