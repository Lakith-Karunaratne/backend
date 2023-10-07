import uvicorn
from fastapi import FastAPI, Depends
from app.env import APPENV
from app.db import database
from app.modules.auth import auth
from app.modules.book_core import book_api

# from initial_data import add_first_user
# from contextlib import asynccontextmanager

# # @asynccontextmanager
# async def lifespan(app: FastAPI):
#     add_first_user()
#     yield
#     print("Admin Created")


app = FastAPI()

app.include_router(auth.router)
app.include_router(book_api.router, dependencies=[Depends(auth.login_manager)])

print(APPENV.get_sql())
# add_first_user()
# @app.on_event("startup")
# async def startupevet():
#     await add_first_user()

@app.get('/')
def root():
    return {"detail":"personal book lib api"}

if __name__ == "__main__":
    PORT = 8000
    uvicorn.run('main:app', port=int(PORT), reload=True)