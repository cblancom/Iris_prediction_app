from fastapi import FastAPI
from api.predict import router
from database.database import create_db_and_tables
import os

print("#" * 50)
print(os.getcwd())


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(router)
