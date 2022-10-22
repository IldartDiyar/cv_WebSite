from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String
from dbmanage.database import DatabaseM

manageObj = DatabaseM()

# manageObj.insertUser("lala", "lala", "lala", "lala", "lala", "lala")
# print(manageObj.GetUserData(2).name)
manageObj.updateUser([2, "lalaas", "lala", "lala", "lala", "lala", "lala"])
print(manageObj.GetUserData(2).name)
