from flask import Flask
from flask_restful import Resource, Api, abort
from flask_cors import CORS
from webargs.flaskparser import parser
from models.Indexer import Indexer
from models.Linker import Linker
from timeit import default_timer as timer

# routes
from routes.Main import Main

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
app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Main, "/api",
endpoint = "api",
resource_class_kwargs={"indexer": wordIndexer})

# Add error handlers
@parser.error_handler
def handle_request_parsing_error(*args):
  abort(400, message="Check query and try again.")