import boto3
from botocore.exceptions import ClientError
import json
from flask import Flask, request
from flask_cors import CORS
from flask_smorest import Api

from resources.csv import blp as CSVBlueprint

app = Flask(__name__)
CORS(app)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Client CSV Uploader"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(CSVBlueprint)