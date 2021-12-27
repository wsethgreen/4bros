from constants import ma


class PlayerSchema(ma.Schema):
    class Meta:
        fields = (
            'player_id',
            'team_id',
            'first_name',
            'last_name',
        )