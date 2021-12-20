from typing import List
from sqlalchemy.sql import text

from constants import(
    Base,
    engine,
    session
)
from data_models.TeamInfo import TeamInfo

teams: List[TeamInfo] = session.query(Base.metadata.tables[TeamInfo.__tablename__]).all()


print(len(teams))