from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()

class user(Base):

    __tablename__ = "userDetails"

    id = Column(Integer, primary_key=True, autoincrement=True)
    userName = Column(String(100))
    password = Column(String(255))
    email = Column(String(100))
    phoneNumber = Column(String)