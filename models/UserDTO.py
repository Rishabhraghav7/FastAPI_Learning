from pydantic import BaseModel


class UserDTO(BaseModel):
    userName : str
    password : str