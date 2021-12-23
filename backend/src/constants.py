from enum import Enum
from sqlalchemy import create_engine
from sqlalchemy.orm import(
    declarative_base,
    sessionmaker
)


# File constants
dynasty_file_path = 'D:\Content\E00001485AECABB5\\454109B6\\00000001\OD-4Bros3'
user_teams = {'Syracuse', 'USC', 'Vanderbilt', 'Wyoming'}


# DB constants
db_path = "sqlite+pysqlite:///backend/ncaa.db?check_same_thread=False"
engine = create_engine(db_path, echo=True, future=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


# Request methods
class HTTPMethods(Enum):
    GET = 'GET'
    POST = 'POST'
