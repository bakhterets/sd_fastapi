from contextlib import asynccontextmanager

from app.api_v1 import router as router_v1
from app.core.config import settings
from app.core.models import Base, db_manager

from fastapi import FastAPI

import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_manager.engine.begin() as con:
        await con.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


@app.get("/")
def hello_root():
    return {
        "message": "Hello root!",
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
