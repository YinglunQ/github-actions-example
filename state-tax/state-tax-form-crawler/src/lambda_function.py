import sys
import os
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '../lib'))

import requests


def lambda_handler(event, context):

    print("Received event:", json.dumps(event, indent=2))

    response = requests.get('https://api.github.com/rate_limit', timeout=5)
    data = response.json()

    print("Response: ", data)

    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }
