from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

import boto3
from botocore.exceptions import ClientError

import json

from schemas import CSVSchema, CSVUpdateSchema

blp = Blueprint("CSVs", __name__, description="User Updated CSV")


@blp.route("/<string:user_id>")
class CSVList(MethodView):
    def get(self, user_id):
        try:
            # Setup s3 client
            boto3.setup_default_session(profile_name="default")
            s3 = boto3.client("s3")

            objects_array = []

            for key in s3.list_objects(
                Bucket="vistar-dc", Prefix=f"2025/01/client-uploads/{user_id}"
            )["Contents"]:
                objects_array.append(key["Key"])

            return objects_array

        except Exception as e:
            print(f"Error: {str(e)}")

@blp.route("/")
class CSV(MethodView):
    def post(self):
            try:
                upload_data = request.get_json()

                print(upload_data)

                json_to_upload = json.dumps(upload_data["json"])

                # Setup s3 client
                boto3.setup_default_session(profile_name="default")

                s3 = boto3.client("s3")
                s3.put_object(
                    Body=json_to_upload,
                    Bucket="vistar-dc",
                    Key=f"2025/01/client-uploads/{upload_data['userId']}/{upload_data['title']}.json",
                )

                return upload_data

            except Exception as e:
                print(f"Error: {str(e)}")