from typing import List
import ncaa_dynasty
import sqlalchemy

from constants import(
    dynasty_file_path,
    user_teams
)


data = ncaa_dynasty.read_database(dynasty_file_path, user_teams)

def_stats = data['Defensive Stats'].records
kicking_stats = data['Kicking Stats'].records
player_info = data['Player Info'].records
commits = data['Committed Recruits'].records
return_stats = data['Return Stats'].records
off_stats = data['Offensive Stats'].records
week_year = data['Week/Year'].records
team_info = data['Team Info'].records
