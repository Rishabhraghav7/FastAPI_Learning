from models.LoginUserDTO import LoginUserDTO
import repository.user_repository as repo  
from models.UsersDTO import UsersDTO
import string
from fastapi import HTTPException
import security.passwordHashing as passwordHashing

def validate_user(userDTO : LoginUserDTO):
    result =repo.findUser(userDTO.userName , userDTO.password)
    if result is None:
        return "Invalid username or password"
    else:
        return "Login sucessfull"


def validate_new_user(user:UsersDTO):
    error = userNameValidation(user.userName)
    if(error):
        return error
    error = passwordValidation(user.password)
    if(error):
        return error
    error = phoneNumberValidation(user.phoneNumber)
    if(error):
        return error
    if(repo.findUserByName(user.userName)is not None):
        raise HTTPException(
            status_code=409 , 
            detail="User already exists")
    if(repo.findUserByEmail(user.email)is not None):
        raise HTTPException(
            status_code=409,
            detail="This E-mail is already registered"
        )
    if(repo.findUserByPhoneNumber(user.phoneNumber) is not None):
        raise HTTPException(
            status_code=409,
            detail="This phone number is already in use"
        )
    user.password = passwordHashing.hashPassword(user.password)
    return repo.addNewUser(user)


def userNameValidation(userName:str):
    result = ""
    if(len(userName)<3 or len(userName)>30):
        result = "The username must be within 3 and 30 characters"
    elif(userName[0] in string.punctuation):
        result= "The username can't start with punctuation"

    return result

def passwordValidation(password :str):
    result = ""
    if(len(password)<6 or len(password)>10):
        result = "The password must be between 6 to 10 characters"
    elif not(any(char.isdigit() for char in password)):
        result = "The password must contain atleast one digit"
    elif not( any(char.isalpha() for char in password)):
        result = "The password must contain atleast one alphabet"
    elif not( any(char in string.punctuation for char in password)):
        result = "The password msut contain atleast one special Character"
    elif not ( any(char.islower() for char in password)):
        result = "The password must contain atleast one lower case character"
    elif not ( any(char.isupper() for char in password)):
        result = "The password must contain atleast one upper case character"

    return result

def phoneNumberValidation(phone: str):
    result = ""
    if(len(phone)!=10):
        result = "The phone number must of 10 characters"
    elif(phone[0]=="0"):
        result = "The phone number can't start with zero"
    elif(not(phone.isdigit())):
        result = "The phone number can contain only numbers"
    return result