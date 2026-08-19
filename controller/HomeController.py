from fastapi import APIRouter
from services.uservalidation import validate_user , validate_new_user
from models.LoginUserDTO import LoginUserDTO
from models.UsersDTO import UsersDTO
router = APIRouter()

@router.get("/home")
def homeController():
    return "welcome Home"

@router.post("/login")
def user_login_details(userDTO : LoginUserDTO ):
    return validate_user(userDTO)

@router.post("/register")
def register_user(userDetails :UsersDTO):
    return validate_new_user(userDetails)