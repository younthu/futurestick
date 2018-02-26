from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBController:

    def get_session():
        return DBSession()


# initialize database connection
engine = create_engine('postgresql://andrewy:@localhost/futuresticks')
DBSession = sessionmaker(bind=engine)
