from typing import List
from constants import(
    Base,
    engine,
    session
)
from data import (
    def_stats,
    kicking_stats,
    player_info,
    commits,
    return_stats,
    off_stats,
    week_year,
    team_info
    )
from data_models.Commits import Commits
from data_models.DefensiveStats import DefensiveStats
from data_models.KickingStats import KickingStats
from data_models.OffensiveStats import OffensiveStats
from data_models.PlayerInfo import PlayerInfo
from data_models.ReturnStats import ReturnStats
from data_models.TeamInfo import TeamInfo
from data_models.WeekYear import WeekYear
from db_scripts import (
    insert_def_stats_into_db,
    insert_player_info_into_db,
    insert_team_info_into_db,
    )


# Create all DB tables
Base.metadata.create_all(engine)


# Insert all data to DB tables
insert_team_info_into_db(team_info)
insert_player_info_into_db(player_info)


players: List[PlayerInfo] = session.query(Base.metadata.tables(PlayerInfo.__tablename__)).all()

print(len(players))
