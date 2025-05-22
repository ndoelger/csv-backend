# Client CSV Uploader

`Client CSV Uploader` contains a boilerplate template in which clients can upload/edit their AWS s3 objects

- List all objects in a user's s3 Bucket (user_id from a test `Auth0`)
- Upload new CSV/JSON data to their s3 Bucket
- Edit JSON data/title of existing object

## How to run

To log into my default aws profile
```sh
$ aws sso login
```
To build/run Docker image

```sh
$ docker build -t csv-uploader .
$ docker run -dp 5001:5001 \                          
  -v $(pwd):/app \
  -v ~/.aws:/root/.aws:ro \
  csv-uploader
```
Open http://localhost:5001/swagger-ui, to test GET/POST/PUT methods. You can use "111930521510381364902" as a test `user_id`. 

## Next Steps

- More streamlined way to connect to AWS without the local profile
- Implementation with Vistar Trafficking Repo
- Flask improvements that align with Vistar standards
  - Error handling
  - Logging
  - Environment configurations
  - Security

## Included modules support

- [`Flask`] — base for application.
- [`boto3`] — for uploading csv data to AWS.
- [`flask_cors`] — grants access to client frontend.
- [`flask_smorest`] — blueprint routing and error handling.
- [`marshmallow`] — object/schema validation.
