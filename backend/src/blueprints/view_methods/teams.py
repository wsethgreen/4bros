from flask import jsonify
from typing import List
from sqlalchemy.ext.serializer import loads, dumps

from constants import(
    engine,
    session
)

from data_models.TeamInfo import TeamInfo
from responses.Teams import TeamSchema


def get_all_teams(request) -> TeamSchema:
    
    teams: List[TeamInfo] = session.query(TeamInfo).all()
    team_schema = TeamSchema()
    teams_json = [team_schema.dump(team) for team in teams]
    
    response = {
        'teams': teams_json
    }
    
    return response


def get_team_by_team_id(request, team_id) -> TeamSchema:
    
    team: TeamInfo = session.query(TeamInfo).where(TeamInfo.team_id == team_id).one()
    team_schema = TeamSchema()
    response: TeamSchema = team_schema.dump(team)
    
    return response
