from pydantic import BaseModel


class LoginUserDTO(BaseModel):
    userName : str
    password : str
    