#so basically ORM means kinda like the interface between the database and the backend, that 
#helps us create our own database table using class 

#self explanatory
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship

from .database import Base #this is the fundamnetal base class we mentioned in the database.py

#-------------- TO CREATE DATABASE (USING ORM)--------------------------------#
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default="True", nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("now()"),
    )
    owner_id = Column(Integer,ForeignKey(
        "users.id", ondelete = "CASCADE"), nullable = False )
    pwner = relationship("User")



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable = False,unique = True)
    password = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("now()"),
    )