from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class TeamInfo(Base):
    __tablename__ = 'team_info'
    team_id = Column(Integer, primary_key=True)
    team_name = Column(String(50))
    team_short_name = Column(String(50))
    coachs_poll_1st_votes = Column(Integer)
    nickname = Column(String(50))
    wins = Column(Integer)
    bcs_rank = Column(Integer)
    coachs_poll_rank = Column(Integer)
    media_poll_rank = Column(Integer)
    losses = Column(Integer)
    media_poll_points = Column(Integer)
    coachs_poll_points = Column(Integer)
