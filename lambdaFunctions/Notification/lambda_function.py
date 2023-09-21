import json
import boto3


def lambda_handler(event, context):
    # TODO implement
    simple1 = event["Records"][0]["Sns"]["Message"]
    response = json.loads(simple1)
    print("Response: ", response)
    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
