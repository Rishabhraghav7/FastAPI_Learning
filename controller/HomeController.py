from fastapi import APIRouter
from models.LoginUserDTO import LoginUserDTO
from models.UsersDTO import UsersDTO
router = APIRouter()
from pydantic import EmailStr
import services.uservalidation as service

@router.get("/home")
def homeController():
    return "welcome Home"

@router.post("/login")
def user_login_details(userDTO : LoginUserDTO ):
    return service.validate_user(userDTO)

@router.post("/register")
def register_user(userDetails :UsersDTO):
    return service.validateNewUser(userDetails)

@router.post("/forget")
def forgetPassword(email:EmailStr):
    return service.forgetPasswordValidation(email)