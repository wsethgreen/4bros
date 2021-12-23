from typing import List

from flask import json
from constants import(
    engine,
    session
)

from data_models.TeamInfo import TeamInfo
from responses.Teams import TeamsGetAllResponse


def get_all_teams(request) -> TeamsGetAllResponse:
    
    teams: List[TeamInfo] = session.query(TeamInfo).all()
    
    # teams_json = [json.dumps(team) for team in teams]
    
    return f'there are {len(teams)} teams.'