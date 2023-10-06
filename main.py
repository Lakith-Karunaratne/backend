import uvicorn
from fastapi import FastAPI
from app.env import APPENV
from app.db import database
# from initial_data import add_first_user
# from contextlib import asynccontextmanager

# # @asynccontextmanager
# async def lifespan(app: FastAPI):
#     add_first_user()
#     yield
#     print("Admin Created")


app = FastAPI()

print(APPENV.get_sql())
# add_first_user()
# @app.on_event("startup")
# async def startupevet():
#     await add_first_user()

if __name__ == "__main__":
    PORT = 8000
    uvicorn.run('main:app', port=int(PORT))