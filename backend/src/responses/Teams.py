
from constants import ma


class TeamSchema(ma.Schema):
    class Meta:
        fields = (
            'team_id',
            'team_name',
            'team_short_name',
            'coachs_poll_1st_votes',
            'nickname',
            'wins',
            'bcs_rank',
            'coachs_poll_rank',
            'media_poll_rank',
            'losses',
            'media_poll_points',
            'coachs_poll_points'
            )
