from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.schema import ForeignKey


Base = declarative_base()

class ReturnStats(Base):
    __tablename__ = 'return_stats'
    player_id = Column(Integer, ForeignKey('player_info.player_id'))
    kick_returns = Column(Integer)
    year = Column(Integer)
    long_kr = Column(Integer)
    punt_returns = Column(Integer)
    long_pr = Column(Integer)
    games_played = Column(Integer)
    kr_tds = Column(Integer)
    pr_tds = Column(Integer)
    kr_yds = Column(Integer)
    pr_yds = Column(Integer)
