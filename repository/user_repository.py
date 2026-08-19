from sqlalchemy import select
from Database.Database import session
from Database.DatabaseUsersDTO import userDTO

# def findUser(userName :str , password: str):
#     db = session()
#     result = db.execute(
#         select(userDTO).where (userDTO.userName == userName , userDTO.password == password)
#         )
#     return result.scalar_one_or_none()

def findUserByName(userName : str):
    db = session()
    result = db.execute(
        select(userDTO).where(userDTO.userName == userName)
    )
    return result.scalar_one_or_none()

def findUserByEmail(email :str):
    db = session()
    result = db.execute(
        select(userDTO).where(userDTO.email == email)
    )
    return result.scalar_one_or_none()

def findUserByPhoneNumber(phone : str):
    db = session()
    result = db.execute(
        select(userDTO).where(userDTO.phoneNumber == phone)
    )
    return result.scalar_one_or_none()

def addNewUser(userDetails:userDTO):
    db = session()
    newUser = userDTO(**userDetails.model_dump())
    db.add(newUser)
    db.commit()
    db.refresh(newUser)

    return newUser
