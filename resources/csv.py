from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
from schemas.csv_schemas import CSVSchema, CSVUpdateSchema

from typing import TypedDict, Optional

import boto3
import json

blp: Blueprint = Blueprint("CSVs", __name__, description="Client Updated CSV")

class CSVUploadDict(TypedDict):
    title: str
    user_id: str
    json: str

class CSVUpdateDict(TypedDict):
    user_id: str
    old_title: Optional[str]
    new_title: Optional[str]
    new_json: Optional[str]

@blp.route("/<string:user_id>")
class CSVList(MethodView):  # GET LIST OF CLIENT CSVS
    def get(self, user_id: str) -> list[str]:
        try:
            # SETUP S3 CLIENT
            boto3.setup_default_session(profile_name="default")
            s3 = boto3.client("s3")

            objects_array: list[str] = []

            # APPEND EACH CSV INTO OBJECTS_ARRAY AND RETURN TO CLIENT
            for key in s3.list_objects(
                Bucket="vistar-dc", Prefix=f"2025/01/client-uploads/{user_id}"
            )["Contents"]:
                objects_array.append(key["Key"])

            return objects_array

        except Exception as e:
            print(f"Error: {str(e)}")


@blp.route("/")
class CSV(MethodView):
    @blp.arguments(CSVSchema)
    def post(self, upload_data: CSVUploadDict) -> CSVUploadDict:  # ADD CSV TO CLIENT BUCKET
        try:
            print(upload_data)

            json_to_upload: str = json.dumps(upload_data["json"])

            # SETUP S3 CLIENT
            boto3.setup_default_session(profile_name="default")
            s3: boto3.client = boto3.client("s3")

            s3.put_object(
                Body=json_to_upload,
                Bucket="vistar-dc",
                Key=f"2025/01/client-uploads/{upload_data['user_id']}/{upload_data['title']}.json",
            )

            return upload_data

        except Exception as e:
            print(f"Error: {str(e)}")

    @blp.arguments(CSVUpdateSchema)
    def put(
        self, upload_data: CSVUpdateDict
    ) -> CSVUpdateDict:  # UPDATE TITLE/JSON OF EXISTING CSV
        try:
            json_to_upload: str = json.dumps(upload_data["new_json"])

            # SETUP S3 CLIENT
            boto3.setup_default_session(profile_name="default")
            s3 = boto3.client("s3")

            # NEED ACCESS
            # s3.copy_object(
            #     Bucket="vistar-dc",
            #     CopySource=f"2025/01/client-uploads/{upload_data['user_id']}/{upload_data['old_name']}.json",
            #     Key=f"2025/01/client-uploads/{upload_data['user_id']}/{upload_data['new_name']}.json",
            # )

            # s3.delete_object(
            #     Bucket="vistar-dc",
            #     Key=f"2025/01/client-uploads/{upload_data['user_id']}/{upload_data['old_name']}.json",
            # )

            s3.put_object(
                Body=json_to_upload,
                Bucket="vistar-dc",
                Key=f"2025/01/client-uploads/{upload_data['user_id']}/{upload_data['new_title']}.json",
            )

            return upload_data
        except Exception as e:
            print(f"Error: {str(e)}")
