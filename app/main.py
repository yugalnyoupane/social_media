from fastapi import FastAPI, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session #helps to interact with the database
from typing import List
from .routers import post, user,auth
#like .add, .commit, .refresh, .delete.query

from . import models, schemas, utils
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Hello World"}




