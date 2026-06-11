#database backbone (that basically connects fastapi with postgresSQL)

from sqlalchemy import create_engine #create_engine basically to build the connection to the database
from sqlalchemy.orm import declarative_base, sessionmaker 
#declarative_bae is used to define database tables using python class
#sessionmaker creates session that talk to the database ( session is basically the worker who taked req, talks to db, brings back results)
from .config import settings
#--------------------------Database Connection-----------------------#

# postgresql://<username>:<password>@<host>/<database>
SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg2://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}'
# "postgresql+psycopg2://postgres:yugal@localhost/fastapi-learn"

engine = create_engine(SQLALCHEMY_DATABASE_URL) #engine is the database connection handler now
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#Session is the temporary connection with the database
#autocommit = false , changes are not saved automatically -> meaning i have to explicitly use db.commit() (meaning saving)
#autoflush = False, prvents automatic sending of changes to DB before commit (meaning pushing to db)
#bind=engine, connecting session to db engine

Base = declarative_base() #base class is the foundation class to build all the table


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#flow explained -> 1. open DB connection, 2. Give it to rout 3. Wait for route to finish, 4. Auto-close connection
