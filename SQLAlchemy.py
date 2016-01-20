#!/usr/bin/python

from sqlalchemy import create_engine, text, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id   = Column(Integer, Sequence('id'), primary_key=True)
    name = Column(String)
    count = Column(Integer)

    def __repr__(self):
        return "<Product(id='%d', name='%s', count='%d')>"%(self.id, self.name, self.count)

DB_CON_STR = 'mysql+mysqldb://root:wangfei@localhost/testdb?charset=utf8'
engine = create_engine(DB_CON_STR, echo=False) #True will turn on the logging

Session = sessionmaker(bind=engine)
session = Session()

#eg1 via class
#res = session.query(Product).filter(Product.id==1).one()
res = session.query(Product).filter(text("id=1")).one()
print res.id, res.name, res.count

ins = session.query(Product)
print ins

#eg2 via sql
sql = text("select * from products")
res = session.execute(sql).fetchall()

for row in res:
        for col in row:
           print col,
        print

session.close()
