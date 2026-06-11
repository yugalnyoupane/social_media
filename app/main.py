from fastapi import FastAPI 
#----------------------importing from files--------------------#
from .routers import post, user,auth
from .database import engine #engine is the connection bridge to your database
from . import models #models actually have our database definitions

models.Base.metadata.create_all(bind=engine) 
# in base class , we define all the table, and .metadata collects all table definitions
# create_all creates tables in DB
# bind = engine tells it which database to use , since in engine in database.py we define the SQLURL

app = FastAPI()

#-----------------including Routers--------------------------#
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Hello World"}




