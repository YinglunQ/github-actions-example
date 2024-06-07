import json


def lambda_handler(event, context):

    print("Received event:", json.dumps(event, indent=2))

    # Return a 200 status with a message
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
