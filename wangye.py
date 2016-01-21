#great tutorial of sqlalchemy
#from http://wangye.org/blog/archives/718/
from sqlalchemy import create_engine

from sqlalchemy import Table, MetaData, Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String
#define engine
engine = create_engine('mysql://root:wangfei@localhost:3306/wangye?charset=utf8', echo=True)

#instance a base
Base = declarative_base()

#define user class 
class User(Base):
     __tablename__ = 'users'
 
     id = Column(Integer, primary_key=True)
     name = Column(String(100))
     fullname = Column(String(100))
     password = Column(String(100))
 
     def __init__(self, name, fullname, password):
         self.name = name
         self.fullname = fullname
         self.password = password
 
     def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)

#commit
Base.metadata.create_all(engine) 