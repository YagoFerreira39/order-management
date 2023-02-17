import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers.base_routers import BaseRouters

app_v1 = BaseRouters.initialize_routes()
app = FastAPI(
    version="0.0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

app.mount("/api/v1", app_v1)

if __name__ == "__main__":
    port = 4001
    uvicorn.run(app, port=port, host="0.0.0.0")
