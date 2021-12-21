from typing import List
from data_models.PlayerInfo import PlayerInfo
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
from db_scripts import (
    insert_def_stats_into_db,
    insert_player_info_into_db,
    insert_off_stats_into_db,
    insert_team_info_into_db,
    )


# Create all DB tables
# Base.metadata.drop_all(bind=engine, tables=[PlayerInfo.__table__])
Base.metadata.create_all(engine)


# Insert all data to DB tables
insert_team_info_into_db(team_info)
insert_player_info_into_db(player_info)
insert_def_stats_into_db(def_stats)
insert_off_stats_into_db(off_stats)
