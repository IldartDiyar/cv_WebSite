from sqlalchemy.orm import Session
import hashlib


def GetData(engine, username, password):
    with Session(engine) as session:
        return session.query(fromio).filter(fromio.username == username, fromio.password == password).first()


def Check_pass(engine, username, password):
    credo = GetData(engine, username, password)

    return credo
