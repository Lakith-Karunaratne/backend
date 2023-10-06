import uvicorn
from fastapi import FastAPI
from app.env import APPENV
from app.db import database

app = FastAPI()

print(APPENV.get_sql())

if __name__ == "__main__":
    PORT = 8000
    uvicorn.run('main:app', port=int(PORT))