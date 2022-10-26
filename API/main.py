from dbmanage.database import DatabaseM
from fastapi import FastAPI

manageObj = DatabaseM()
app = FastAPI()


@app.get("/")
async def root():
    return manageObj.true

# get data from User


@app.get("/get_data/User/{id}")
async def GetData(id: int):
    return manageObj.GetUserData(id)


# get data from CV
@app.get("/get_data/Cv/{id}")
async def GetData(id: int):
    return manageObj.GetCvData(id)

# checking passwor


@app.get("/check_password/")
async def GetData(username: str, password: str):
    db = manageObj.CheckPassword(username, password)
    return db


@app.post("/InsertDataUser/")
async def InsertDataUser(usernamemio: str, namemio: str, lnamemio: str, phonemio: str, passwordio: str, emailio: str):
    db = manageObj.insertUser(usernamemio, namemio,
                              lnamemio, phonemio, passwordio, emailio)
    return db


@app.post("/InsertDataCv/")
async def InsertDataCv(id_userio: str, stackio: str, job_experience: str, githublink: str):
    db = manageObj.insertUser(usernamemio, namemio,
                              lnamemio, phonemio, passwordio, emailio)
    return db


@app.delete("/DeleteUser/{id}")
async def DeleteUser(id: int):
    db = manageObj.deleteUserData(id)
    return db


@app.delete("/DeleteCv/{id}")
async def DeleteUser(id: int):
    db = manageObj.deleteCvData(id)
