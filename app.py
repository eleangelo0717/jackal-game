from flask import Flask, escape, request, jsonify
from flask_cors import CORS

from gameserver import GameServer
from common.utils import GameEncoder

app = Flask(__name__)
CORS(app)
app.json_encoder = GameEncoder

GS = {}


@app.route('/games/')
def games():
    return f'{len(GS)}'


@app.route('/games/<id>', methods=['GET', 'POST'])
def game(id):
    game = GS.get(id, GameServer())

    if (request.method == 'POST') and (request.is_json):
        data = request.get_json()
        item = int(data.get('item'))
        x = int(data.get('x'))
        y = int(data.get('y'))
        success = game.move(item, x, y)
        result = game.to_json()
        result['success'] = success

        return jsonify(result)

    return jsonify(
        game.to_json()
    )


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
