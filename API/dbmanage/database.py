from dbmanage.models import *
from dbmanage.crud import *
from dbmanage.retrive import *
from sqlalchemy import create_engine

db = 'postgresql://postgres:postgres@localhost:5432/PythonProject'


class DatabaseM:
    def __init__(self):
        self.engine = create_engine(db, echo=False, future=True)
        Base.metadata.create_all(self.engine)

    def insertUser(self, usernamemio, namemio, lnamemio, phonemio, passwordio, emailio) -> bool:
        iin = User(username=usernamemio, name=namemio, lname=lnamemio, phone=phonemio,
                   password=passwordio, email=emailio)
        return (create_entry([iin], self.engine))

    def deleteUser(self, id) -> bool:
        return delete(GetData(self.engine, id, User), self.engine)

    def updateUser(self, new_value) -> bool:
        Data = GetData(self.engine, new_value[0], User)
        return update([Data], new_value, self.engine)

    def GetUserData(self, id):
        return GetData(self.engine, id, User)
