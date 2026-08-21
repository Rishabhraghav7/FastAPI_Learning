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

@PATHVARIABLE & @PARAMBODY

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

nothing called parambody just direct mapping.

@GETMAPPING 

@GetMapping("/path") is just replaced with 
@app.get("/path") nothing much complex 

SQL ALCHEMY 

first we are creating a session using the sessionmaker() like using the connection in the JDBC 

engine is like DriverManager 
and the query is like preparedstatement in JDBC 

 In SpringBoot we move to JDBC template or JDBC namedtemplate 
replacing the plain JDBC and the connection and session creation is also not like this but in both namedtemplate and template we write query like :id , :name , :email but in python we just use functions like add() , etc directly and the query part is handled by the sqlalchemy 

also we use the same DTO to carry the data till the repo and fetch it from the repo in python we use 2 DTO one for the carrying part and another is just a replica of the db structure and each time we convert from the 
normal DTO -> DB replica DTO 

This DB replica DTO extends a class called Base which is from the 

```
from sqlalchemy.ext.declarative import declarative_base
base = declarative_base()
```
and once you extend this base the class object declaration becomes a little different 
we use = replacing : 
id : int is written like id = column( Integer , primary_key = true )
here the data type follows like the SQL DB we use. 
for string data type we mention the size like Column(String(225))

@id which we use for primary key reference in java is replaced with primary_key = True and it is parameter 
 @Table(name ="Table name") is replaced with _ _tablenmae_ _ = "table name" 

HTTPException

instead of using try catch and returning the error as a dict type use this 
it has parameter status_code used to return the desired one , 
detail= the error message you would like to return or the data,
not yet used (headers = when you need to pass additional info like info on bearer tokens , rate limiting , retry timings. )

Password Hashing 

Used Argon2 to hash the password 
```
from argon2 import PasswordHasher

class passwordHashing:
    hasher = PasswordHasher(
        time_cost=3,
        memory_cost=65536,
        parallelism=4,
        hash_len=32,
        salt_len=16
    )
```

time_cost -> how many cycles to repeat the process
memory_cost -> in KIB how much memory to allocate 
parallelism -> how many threads to run dividing the process
hash_len -> lenght of password = 32 * 8 = 256 bits
salt_len -> random character added so that db allows same password = 16 * 8 = 128 bits 

to hash password use .hash(password)
to verify use .verify(hashed_password, password ) 
don't hash the password and then check with hashed_password since each time salt value changes it creates new hash value and they never are true just use .verify()


