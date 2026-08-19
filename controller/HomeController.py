from fastapi import APIRouter
router = APIRouter()

@router.get("/home")
def homeController():
    return "welcome Home"