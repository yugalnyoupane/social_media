from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
#--------------------------Database Connection-----------------------#

# postgresql://<username>:<password>@<host>/<database>
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:yugal@localhost/fastapi-learn"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
