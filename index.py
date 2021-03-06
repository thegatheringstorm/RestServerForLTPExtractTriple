# coding:utf-8

from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

from relation_triple_extraction_RULE import LTPExtractTriple
from config import MODELDIR
import urllib

app = Flask(__name__)
CORS(app)
api = Api(app)

LTPExtractTripleInstance = LTPExtractTriple(MODELDIR)

class LTPExtractTripleAPI(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('UserInput', type=str, help='UserInput')
        args = parser.parse_args()
        UserInput = urllib.unquote(args['UserInput']).split('\n')

        result = LTPExtractTripleInstance.pack(UserInput)

        return {'Result': result}


api.add_resource(LTPExtractTripleAPI, '/')

if __name__ == '__main__':
    app.run(port=1234)
