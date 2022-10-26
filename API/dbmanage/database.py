from dbmanage.models import *
from dbmanage.crud import *
from dbmanage.retrive import *
from sqlalchemy import create_engine

db = 'postgresql://postgres:postgres@localhost:5432/PythonProject'


class DatabaseM:
    def __init__(self):
        self.engine = create_engine(db, echo=False, future=True)
        Base.metadata.create_all(self.engine)
        self.true = True

    def insertUser(self, usernamemio, namemio, lnamemio, phonemio, passwordio, emailio) -> bool:
        iin = User(username=usernamemio, name=namemio, lname=lnamemio, phone=phonemio,
                   password=passwordio, email=emailio)
        return (create_entry([iin], self.engine))

    def deleteUserData(self, id) -> bool:
        return delete(GetData(self.engine, id, User), self.engine)

    def deleteCvData(self, id) -> bool:
        return delete(GetData(self.engine, id, Cv), self.engine)

    def updateUser(self, new_value, fromio) -> bool:
        Data = GetData(self.engine, new_value[0], fromio)
        return updatio(Data, new_value, self.engine)

    def GetUserData(self, id):
        return GetData(self.engine, id, User)

    def CheckPassword(self, username, password):
        return Check_pass(self.engine, username, password)

    def insertCv(self, id_userio, stackio, job_experience, githublink) -> bool:
        iin = Cv(id_user=id_userio, stack=stackio,
                 job_experience=job_experiencio, githublink=githublinkio)
        return (create_entry([iin], self.engine))

    def GetCvData(self, id):
        return GetData(self.engine, id, Cv)
