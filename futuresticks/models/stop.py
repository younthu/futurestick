from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from .DBController import DBController


Base = declarative_base()


class Stop(Base):
    __tablename__ = 'stop'

    # table schema
    id = Column(Integer, autoincrement=True, primary_key=True)
    code = Column(String('20'))
    num = Column(Integer)
    price = Column(Float)
    status = Column(Boolean)
    description = Column(String('1000'))

    def stop_order(code, stop, num):
        session = DBController.get_session()
        new_trade = Stop(code=code, num=num, price=stop, status=False)
        session.add(new_trade)
        session.commit()
        session.close()
