from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.schema import ForeignKey


Base = declarative_base()

class KickingStats(Base):
    __tablename__ = 'kicking_stats'
    player_id = Column(Integer, ForeignKey('player_info.player_id'))
    fg_made_17_29 = Column(Integer)
    fg_att_17_29 = Column(Integer)
    long_fg = Column(Integer)
    ko_touchbacks = Column(Integer)
    long_punt = Column(Integer)
    xp_att = Column(Integer)
    year = Column(Integer)
    punts_blocked = Column(Integer)
    fg_att = Column(Integer)
    total_punt_yards = Column(Integer)
    fg_att_17_29 = Column(Integer)
    xp_blocked = Column(Integer)
    fg_blocked = Column(Integer)
    fg_att_40_49 = Column(Integer)
    fg_made_40_49 = Column(Integer)
    fg_att_30_39 = Column(Integer)
    fg_made_30_39 = Column(Integer)
    fg_att_50_plus = Column(Integer)
    fg_made_50_plus = Column(Integer)
    punt_touchbacks = Column(Integer)
    games_played = Column(Integer)
    kickoffs = Column(Integer)
    xp_made = Column(Integer)
    net_punting = Column(Integer)
    fg_made = Column(Integer)
    number_punts = Column(Integer)
    inside_twenty = Column(Integer)