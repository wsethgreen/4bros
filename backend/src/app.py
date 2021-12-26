from constants import app
from blueprints.teams import teams_bp



blueprints = [
    teams_bp
]


app.register_blueprint(teams_bp, url_prefix=f'/teams')

app.route('', methods=['GET', 'POST'])
def hello():
    return 'hello'


if __name__ == '__main__':
    app.run(debug=True)
