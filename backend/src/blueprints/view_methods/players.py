from typing import List

from constants import session

from data_models.PlayerInfo import PlayerInfo
from responses.Players import PlayerSchema


player_schema = PlayerSchema()


def get_all_players(request):
    
    players: List[PlayerInfo] = session.query(PlayerInfo).all()
    players_json = [player_schema.dump(player) for player in players]
    
    response = {
        'players': players_json
    }
    
    return response


def get_player_by_player_id(request, player_id) -> PlayerSchema:
    player: PlayerInfo = session.query(PlayerInfo).where(
        PlayerInfo.player_id == player_id).one()
    response = player_schema.dump(player)
    
    return response


def get_players_by_team_id(request, team_id):
    players: List[PlayerInfo] = session.query(PlayerInfo).filter(
        PlayerInfo.team_id == team_id).all()
    players_json = [player_schema.dump(player) for player in players]
    
    response = {
        'players': players_json
    }
    
    return response
