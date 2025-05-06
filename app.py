import boto3
from botocore.exceptions import ClientError
import json
import requests
from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

S3_URL = (
    "https://vistar-dc.s3.us-east-1.amazonaws.com/2024/11/prizepicks/nba_dates.json"
)


# @app.get("/")
# def get_data():
#     try:
#         response = requests.get(S3_URL)
#         # print(response)
#         body = response.json()
#         # print(body)

#         string = json.dumps(body)
#         # print(string)

#         # Setup s3 client
#         boto3.setup_default_session(profile_name="default")

#         s3 = boto3.client("s3")
#         s3.put_object(Body=string, Bucket="vistar-dc", Key="2025/01/aws-cache/hey")
#         return body

#     except Exception as e:
#         print(f"Error: {str(e)}")


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
