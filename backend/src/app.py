from blueprints.players import players_bp
from blueprints.stats import stats_bp
from blueprints.teams import teams_bp
from constants import app


blueprints = [
    players_bp,
    stats_bp,
    teams_bp,
]

for bp in blueprints:
    app.register_blueprint(bp, url_prefix=f'/{bp.name}')


app.route('', methods=['GET', 'POST'])
def hello():
    return 'hello'


if __name__ == '__main__':
    app.run(debug=True)
