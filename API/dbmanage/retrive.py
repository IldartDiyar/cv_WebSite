from sqlalchemy.orm import Session


def GetData(engine, id, fromio):
    with Session(engine) as session:
        return session.query(fromio).filter(fromio.id == id).first()
