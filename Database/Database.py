from sqlalchemy.orm import sessionmaker as session
from sqlalchemy import create_engine 
from Database.DatabaseUsersDTO import Base

db_url = "mysql+pymysql://root:YourNewPassword123!@localhost:3306/fastapi_learning"
engine = create_engine(db_url)

session = session(autocommit = False, autoflush= False , bind = engine)

# first time to create a table in MySQL
def initializeDB():
    Base.metadata.create_all(bind = engine)
# use just once to create the table 
# initializeDB()
