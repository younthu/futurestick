from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from .DBController import DBController

Base = declarative_base()


class Trade(Base):
    __tablename__ = 'trade'

    # table schema
    id = Column(Integer, autoincrement=True, primary_key=True)
    code = Column(String('20'))
    num = Column(Integer)
    price = Column(Float)
    description = Column(String('1000'))

    def trade(code, num, price):
        session = DBController.get_session()
        new_trade = Trade(code=code, num=num, price=price)
        session.add(new_trade)
        session.commit()
        session.close()
