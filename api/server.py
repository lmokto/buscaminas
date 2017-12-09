from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS

import json
from game import generate_buscaminas, LEVELS, filter_by_key

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')


class UpdateGame(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def post(self):
        pass


class GenerateGame(Resource):
    def get_mines(self, game):
        return filter_by_key(game, key="mine", equal=[True])

    def get_numbers(self, game):
        return filter_by_key(game, key="number", equal=list(range(1, 9)))

    def get_spaces(self, game):
        return filter_by_key(game, key="number", equal=['space'])

    def schema_api(self, game):
        return {
            'mines': self.get_mines(game),
            'numbers': self.get_numbers(game),
            'spaces': self.get_spaces(game)
        }

    def get(self, level):
        game = generate_buscaminas(level=level)
        dimension = LEVELS.get(level).get('dimension')
        schema = self.schema_api(game)
        return jsonify(**{
            'id': 1,
            'dimension': dimension,
            'mines': schema.get('mines'),
            'numbers': schema.get('numbers'),
            'spaces': schema.get('spaces')
        })


api.add_resource(GenerateGame, '/api/generate/<level>')
#api.add_resource(UpdateGame, '/update/<id>')

if __name__ == '__main__':
    app.run(debug=True)
