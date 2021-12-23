from flask import Response
from typing import List

from data_models.TeamInfo import TeamInfo

class TeamsGetAllResponse(Response):
    teams = List[TeamInfo]