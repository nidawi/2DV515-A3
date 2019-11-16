from flask import Flask
from flask_restful import Resource, Api
from models.Indexer import Indexer
from models.Linker import Linker
from timeit import default_timer as timer
import os

# This is my first time ever using python for anything more than
# "Hello, World!". Do not expect miracles.
# Also, I am not aware of any code standards for python.
# Also, I am using Python v. 3.8.0

# start timer
startTime = timer()

# create out link manager
linksFolder = "wikipedia/Links"
linkManager = Linker(linksFolder)
# create our word indexer
wordFolder = "wikipedia/Words"
wordIndexer = Indexer(wordFolder, linkManager)

# end timer and notify loading finished
endTime = timer()
print("Finished loading and calculating page ranks in %s seconds." % round((endTime - startTime), 2))

# continue normal procedure when everything is loaded
result = wordIndexer.search_test("java programming")

for res in result:
  print(res.jsonify())

# wordIndexer.search("java")[0:5]
# wordIndexer.search_test()

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
  def get(self):
    return { "Hello": "World" }

# dd

api.add_resource(HelloWorld, "/")