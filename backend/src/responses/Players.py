from marshmallow import fields, Schema


class PlayerSchema(Schema):
    class Meta:
        fields = (
            'player_id',
            'team_id',
            'first_name',
            'last_name',
        )