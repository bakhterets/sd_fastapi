from contextlib import asynccontextmanager

from app.core.models import Base, db_manager

from fastapi import FastAPI

import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_manager.engine.begin() as con:
        await con.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def hello_root():
    return {
        "message": "Hello root!",
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
