from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer, String,create_engine

Base=declarative_base()

class Smartphone(Base):
    __tablename__='smartphone'

    id=Column(Integer,primary_key=True,autoincrement=True )
    brand=Column(String)
    name=Column(String)
    price=Column(Integer)
    ram=Column(Integer)
    storage=Column(Integer)

if __name__=='__main__':
    engine=create_engine('sqlite:///mydatabase.sqlite3')
    Base.metadata.create_all(engine)