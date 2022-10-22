from sqlalchemy.orm import Session


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


def update(models: list, new_value: list, engine):
    try:
        with Session(engine) as session:
            for keys, x in models, range(new_value):
                asd = models.keys
                asd1 = new_value[x]
                models.keys = new_value[x]
                print(asd, " ", asd1)
                session.commit()
            return True
    except:
        return False
