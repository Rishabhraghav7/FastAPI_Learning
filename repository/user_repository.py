from sqlalchemy import select
from Database.Database import session
from Database.DatabaseUsersDTO import user

def findUser(userName :str , password: str):
    db = session()
    result = db.execute(
        select(user).where (user.userName == userName , user.password == password)
        )
    return result.scalar_one_or_none()

def findUserByName(userName : str):
    db = session()
    result = db.execute(
        select(user).where(user.userName == userName)
    )
    return result.scalar_one_or_none()

def findUserByEmail(email :str):
    db = session()
    result = db.execute(
        select(user).where(user.email == email)
    )
    return result.scalar_one_or_none()

def findUserByPhoneNumber(phone : str):
    db = session()
    result = db.execute(
        select(user).where(user.phoneNumber == phone)
    )
    return result.scalar_one_or_none()
