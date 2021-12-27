from typing import List

from constants import session

from data_models.OffensiveStats import OffensiveStats
from data_models.PlayerInfo import PlayerInfo

from responses.Stats import PassingStatsSchema


def get_season_passing_stats(request):
    
    players = session.query(PlayerInfo).join(OffensiveStats).where(
        PlayerInfo.player_id == OffensiveStats.player_id).all()
    passing_stats_schema = PassingStatsSchema()
    players_json = [passing_stats_schema.dump(player) for player in players]
    
    response = {
        'players': players_json
    }
    
    return response
