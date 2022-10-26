from sqlalchemy.orm import Session
from sqlalchemy import update


def create_entry(models: list, engine) -> bool:
    try:
        with Session(engine) as session:
            session.add_all(models)
            session.commit()
            return True
    except:
        return False


def delete(models: list, engine):
    try:
        with Session(engine) as session:
            session.delete(models)
            session.commit()
            return True
    except:
        return False


def updatio(models: list, new_value: list, engine):
    try:
        with Session(engine) as session:
            models.update(new_value,  synchronize_session=False)
            session.commit()
            session.refresh()
    except:
        return False
