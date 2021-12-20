from sqlalchemy import create_engine
from sqlalchemy.orm import(
    declarative_base,
    sessionmaker
)


# File constants
dynasty_file_path = 'D:\Content\E00001485AECABB5\\454109B6\\00000001\OD-4Bros3'
user_teams = {'Syracuse', 'USC', 'Vanderbilt', 'Wyoming'}


# DB constants
engine = create_engine("sqlite+pysqlite:///backend/ncaa.db", echo=True, future=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
