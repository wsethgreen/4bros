from constants import ma
from marshmallow import fields

from data_models.OffensiveStats import OffensiveStats


class PassingStatsSchema(ma.Schema):
    class Meta:
        fields = (
            'player_id',
            'first_name',
            'last_name',
            fields.Nested(OffensiveStats(only=('pass_yards'))),
            'longest_pass',
            'year',
            'pass_tds',
            'games_played',
            'completions',
            'ints',
            'pass_att',
        )