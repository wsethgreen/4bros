from typing import List
from sqlalchemy.sql import exists

from data import(
    def_stats,
    player_info,
    off_stats,
    team_info,
    week_year
)
from constants import(
    Base,
    engine,
    session
)
from data_models.DefensiveStats import DefensiveStats
from data_models.PlayerInfo import PlayerInfo
from data_models.OffensiveStats import OffensiveStats
from data_models.TeamInfo import TeamInfo



jared_yates = session.query(PlayerInfo).filter(PlayerInfo.player_id == 8106).one()
print(jared_yates)
jared_yates_off_stats = session.query(OffensiveStats).filter(OffensiveStats.player_id == jared_yates.player_id).one()
print(jared_yates_off_stats)

players: List[PlayerInfo] = session.query(PlayerInfo).filter(
    PlayerInfo.team_id == 115).all()

print(players[:10])


### 
# Check for length of dictionary records compared to DB records
###

# print(f'Team Dict Records: {len(team_info)}')
# print(f'Team DB Records: {len(teams)}')
# print(f'Player Info Dict Records: {len(player_info)}')
# print(f'Player Info DB Records: {len(players)}')
# print(f'Player Def Stats Dict Records: {len(def_stats)}')
# print(f'Player Def Stats DB Records: {len(defensive_stats_all)}')
# print(f'Player Off Stats Dict Records: {len(off_stats)}')
# print(f'Player Off Stats DB Records: {len(offensive_stats_all)}')
