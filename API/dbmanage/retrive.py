from sqlalchemy.orm import Session
import hashlib


def GetDataByPass(engine, username, password):
    with Session(engine) as session:
        return session.query(fromio).filter(fromio.username == username, fromio.password == password).first()


def GetData(engine, id, fromio):
    with Session(engine) as session:
        return session.query(fromio).filter(fromio.id == id).first()


def Check_pass(engine, username, password):
    credo = GetDataByPass(engine, username, password)

    return credo
