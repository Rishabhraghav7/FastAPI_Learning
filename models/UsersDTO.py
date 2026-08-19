from pydantic import BaseModel , EmailStr
class UsersDTO(BaseModel):
        id : int
        userName : str
        password : str
        email : EmailStr
        phoneNumber:str