from flask import Flask, escape, request, jsonify

from gameserver import GameServer

app = Flask(__name__)

GS = {}


@app.route('/games/')
def games():
    return f'{len(GS)}'


@app.route('/games/<id>')
def game(id):
    game = GS.get(id, GameServer())
    return jsonify(
        game.toDict()
    )
