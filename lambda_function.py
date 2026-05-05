import boto3
import os
from datetime import datetime
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('image_metadata_table')

def lambda_handler(event, context):
    try:
        for record in event['Records']:
            bucket_name = record['s3']['bucket']['name']
            object_key = record['s3']['object']['key']
            object_size = record['s3']['object']['size']

            file_extension = os.path.splitext(object_key)[1]

            image_id = str(uuid.uuid4())[:8]
            upload_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

            table.put_item(
                Item={
                    'image_id': image_id,
                    'file_name': object_key,
                    'file_size': str(object_size),
                    'file_type': file_extension,
                    'upload_time': upload_time,
                    'bucket_name': bucket_name
                }
            )

        return {
            'statusCode': 200,
            'body': 'Metadata stored successfully'
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
