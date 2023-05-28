from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#executing the instructions from the database

db = create_engine("postgresql:///databasename")
base = declarative_base()

#create a class-based model for the 'ClassName' table
class ClassName(base):
    __tablename__ = "ClassName"
    ClassNameId = Column(Integer, primary_key=True)
    Name = Column(String)

#create a class-based model for the 'SecondClassName' table
class SecondClassName(base):
    __tablename__ = "SecondClassName"
    SecondClassNameId = Column(Integer, primary_key=True)
    Title = Column(String)
    ClassNameId = Column(Integer, ForeignKey("ClassName.ClassNameId"))

#create a class-based model for the 'ThirdClassName' table
class ThirdClassName(base):
    __tablename__ = "ThirdClassName"
    ThirdClassNameId = Column(Integer, primary_key=True)
    Title = Column(String)
    SecondClassNameId = Column(Integer, ForeignKey("SecondClassName.SecondClassNameId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)



#instead of connecting to the database directly, we will ask for a session
#create a new instance of sessionmaker, then point to our engine (the db)

Session = sessionmaker(db)

#opens an actual session by calling the Session() subclass defined above-this time lowercase s

session = Session()

#creating the database subclass using the declarative base subclass and generate all metadata

base.metadata.create_all(db)

#Query 1 (sample query based on Chinook) select all records from 'ClassName' table:

artists = session.query(ClassName)
for artist in artists:
    print(artist.ClassNameId, artist.Name, sep = " | ")




