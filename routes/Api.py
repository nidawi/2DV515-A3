from flask_restful import Resource

class Api(Resource):
  def __init__(self, indexer):
    self.indexer = indexer