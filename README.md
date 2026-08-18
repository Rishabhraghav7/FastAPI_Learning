```
app = FastAPI()

@app.get("/path")
def funct()
	return 
```
all under main.py
an application object is created 
this app holds the application a kind of reference allows to be used with methods like get etc 

when the folder and file structure is to be maintained like a springBoot one we split it into DTO(models) , controller , Service , Repo if needed one folder for messaging queues or brokers 

so when we split here we use APIRouter()

```
from fastapi import APIRouter
router = APIRouter()
@router.get("/home")

def homeController():
    return 
```
this router creates a router registry 
a route object is like {path : "/home" , method : "GET"} 

```
app.include_router(router)
```
 we use this in the main.py and import the router from the HomeController.py file 
 app.include_router(router) iterates through router.routes and clones them into app.router.routes
 
 when the uvicorn server starts and hits the app it app.router matches the home path and get method and executes the homeController 
 
 ```
 main.py
   ↓
app = FastAPI()
   ↓
app.include_router(router)
   ↓
controller/home_controller.py
   ↓
GET /home
   ↓
homeController()
   ↓
"welcome"
 ```
 
 when compared with springBoot 
 ```
 Spring Boot                         FastAPI

@SpringBootApplication       →      app = FastAPI()

@RestController              →      APIRouter()

@GetMapping("/home")         →      @router.get("/home")

Controller class             →      controller module/file

Spring Boot application      →      main.py
 ```