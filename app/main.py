from fastapi import FastAPI

from app.api_v1.endpoints.posts import router
from app.api_v1.endpoints.users import fastapi_users, auth_backend
from app.db.session import create_db_and_tables
from app.schemas.users import UserCreate, UserRead

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/token",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/register',
    tags=['register']
)

app.include_router(router,
                   prefix='/posts',
                   tags=['posts'])


@app.on_event("startup")
async def on_startup():
    # Not needed if you setup a migration system like Alembic
    await create_db_and_tables()
