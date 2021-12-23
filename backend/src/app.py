from flask import Flask
from flask_cors import CORS

from blueprints.teams import teams_bp

app = Flask(__name__)
CORS(app)

blueprints = [
    teams_bp
]


app.register_blueprint(teams_bp, url_prefix=f'/teams')

app.route('', methods=['GET', 'POST'])
def hello():
    return 'hello'


if __name__ == '__main__':
    app.run(debug=True)
