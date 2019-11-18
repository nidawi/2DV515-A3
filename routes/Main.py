from flask_restful import Resource
from models.Indexer import Indexer
from webargs import fields, validate
from webargs.flaskparser import use_args, use_kwargs, parser
from base64 import b64decode

class Main(Resource):
  args = {
    "query": fields.Raw(
      required=True,
      validate=validate.Length(1, max=None)
    ),
    "count": fields.Int(
      required=False,
      validate=validate.Range(1, max=None)
    )
  }

  def __init__(self, indexer: Indexer):
    self.__indexer = indexer

  @use_args(args)
  def get(self, args):
    queryResult = self.__indexer.query(args["query"])

    if "count" in args:
      return queryResult.jsonify(count = args["count"])
    else:
      return queryResult.jsonify()
    