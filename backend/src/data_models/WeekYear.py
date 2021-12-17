from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class WeekYear(Base):
    __tablename__ = 'week_year'
    week = Column(Integer)
    year = Column(Integer)

WeekYear.__table__