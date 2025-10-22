from fastapi import FastAPI
from contextlib import asynccontextmanager
from .api.routers import user_router
from src.app.config import Config

config = Config()


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.config = config
    yield


app = FastAPI(title="RPG sim", debug=True, lifespan=lifespan)
app.include_router(user_router.router)
