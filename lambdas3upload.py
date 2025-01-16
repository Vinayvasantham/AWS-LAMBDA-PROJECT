import base64
import boto3
import json

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        bucket_name = event['bucket_name']
        file_name = event['file_name']
        file_content = event['file_content']  # Base64-encoded content

        # Decode the Base64 content
        decoded_file = base64.b64decode(file_content)

        # Upload the file to S3
        s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=decoded_file)

        return {
            'statusCode': 200,
            'body': json.dumps({'message': f"File {file_name} successfully uploaded to {bucket_name}"})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
