import boto3
from botocore.exceptions import ClientError
import json
from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.get("/")
def get_data():
    try:
        # Setup s3 client
        boto3.setup_default_session(profile_name="default")
        s3 = boto3.client("s3")

        user_id = "111930521510381364902"
        title = "Test"

        response = s3.get_object(
            Bucket="vistar-dc", Key=f"2025/01/client-uploads/{user_id}/{title}.json"
        )

        body = response["Body"].read()

        return body

    except Exception as e:
        print(f"Error: {str(e)}")


@app.post("/")
def upload_test():
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
