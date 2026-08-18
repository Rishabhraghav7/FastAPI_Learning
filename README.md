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

PYDANTIC 

This package is mainly used for data validation purpose also to parse data
from this package import BaseModel 
extend the the pojo / DTO / Model with this class this take care of the creation of the _ _init_ _ i.e the constructor part this also rises error when the parameters are not specified with correct values by default python is not as rigid as java with class declaration and data types for class members so pydantic helps here .

@PATHVARIABLE

```
@GetMapping("/user/{id}")
public String getUser(@PathVariable int id) {
    return "User ID: " + id;
}
```

in java we use a placeholder in the api path then map it to the function's parameter using the @PathVariable annotation but in python 

```
@app.get("user/{id}")
def func(id:int):
	return 
```
direct mapping with the parameter and the placeholder just make sure names are same .

@GETMAPPING 

@GetMapping("/path") is just replaced with 
@app.get("/path") nothing much complex 

