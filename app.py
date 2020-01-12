from flask import Flask, escape, request, jsonify

from gameserver import GameServer
from common.utils import GameEncoder

app = Flask(__name__)
app.json_encoder = GameEncoder

GS = {}


@app.route('/games/')
def games():
    return f'{len(GS)}'


@app.route('/games/<id>')
def game(id):
    game = GS.get(id, GameServer())
    return jsonify(
        game.to_json()
    )
