from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    name = Column(String(50))
    lname = Column(String(50))
    phone = Column(String(11))
    password = Column(String(64))
    email = Column(String(50))


class Cv(Base):
    __tablename__ = 'cv'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey("users.id"))
    stack = Column(String(25))
    job_experience = Column(Integer)
    githublink = Column(String(255))
