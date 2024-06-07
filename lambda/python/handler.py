import json
import boto3
import requests
import time

def s3_handler(event, context):
    s3 = boto3.client('s3')

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        # Call a demo external endpoint
        response = requests.post('https://jsonplaceholder.typicode.com/posts', json={
            'bucket': bucket,
            'key': key
        })

        print(f'File {key} uploaded to {bucket}. Endpoint response: {response.status_code}, {response.json()}')

        # Wait for 5 seconds and print a message every second
        for i in range(5):
            print(f'Waiting... {i+1} seconds')
            time.sleep(1)

        # Delete the uploaded file from the S3 bucket
        s3.delete_object(Bucket=bucket, Key=key)
        print(f'File {key} deleted from {bucket}')

    result = {
        'statusCode': 200,
        'body': json.dumps('Build successful')
    }
    print(f'Returning result: {result}')
    return result
