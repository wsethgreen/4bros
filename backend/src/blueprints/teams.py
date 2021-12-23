from flask import Blueprint, request
from responses.Teams import TeamsGetAllResponse

from constants import HTTPMethods

from data_models.TeamInfo import TeamInfo
from blueprints.view_methods.teams import(
    get_all_teams,
)

teams_bp = Blueprint('teams', __name__)


@teams_bp.route('', methods=['GET'])
def teams_get_all() -> TeamsGetAllResponse:
    return get_all_teams(request)
