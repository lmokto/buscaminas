from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
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

    def get(self):
        return {
            'id': 1,
            'dimension': {},
            'mines': [],
            'numbers': []
        }


api.add_resource(GenerateGame, '/generate')
api.add_resource(UpdateGame, '/update/<id>')

if __name__ == '__main__':
    app.run(debug=True)
