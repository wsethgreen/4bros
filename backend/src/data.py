import ncaa_dynasty
import sqlalchemy

dynasty_file_path = 'D:\Content\E00001485AECABB5\\454109B6\\00000001\OD-4Bros3'
user_teams = {'Syracuse', 'USC', 'Vanderbilt', 'Wyoming'}

data = ncaa_dynasty.read_database(dynasty_file_path, user_teams)

def_stats = data['Defensive Stats']
kicking_stats = data['Kicking Stats']
player_info = data['Player Info']
commits = data['Committed Recruits']
return_stats = data['Return Stats']
off_stats = data['Offensive Stats']
week_year = data['Week/Year']
team_info = data['Team Info']



for key in week_year.records[0].fields:
    print(key)

# for record in player_info.records[0:2]:
#     print(record.fields)