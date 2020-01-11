import json

class GameEncoder(json.JSONEncoder):
    # pylint: disable=method-hidden
    def default(self, obj):
        if "to_json" in dir(obj):
            return obj.to_json()
        return json.JSONEncoder.default(self, obj)

def distance(a, b):
    return abs(b - a)