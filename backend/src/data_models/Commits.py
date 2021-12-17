from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class Commits(Base):
    __tablename__ = 'commits'
    stars = Column(Integer)
    name = Column(String(50))
    position = Column(String(50))
    rank = Column(Integer)
    school = Column(String(50))
