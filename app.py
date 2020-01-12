from flask import Flask, escape, request, jsonify

from gameserver import GameServer
from common.utils import GameEncoder

app = Flask(__name__)
app.json_encoder = GameEncoder

GS = {}


@app.route('/games/')
def games():
    return f'{len(GS)}'


@app.route('/games/<id>', methods=['GET', 'POST'])
def game(id):
    game = GS.get(id, GameServer())
    if request.method == 'POST':
        item = int(request.form.get('item'))
        x = int(request.form.get('x'))
        y = int(request.form.get('y'))
        success = game.move(item, x, y)
        result = game.to_json()
        result['success'] = success
        if not (success):
            return jsonify(result)
    return jsonify(
        game.to_json()
    )
