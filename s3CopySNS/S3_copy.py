import boto3
import os
import json

sns_client = boto3.client('sns')

def lambda_handler(event, context):
    #had to google Event message structure
    file_name = event['Records'][0]['s3']['object']['key']
    service_name='s3'
    region_name='us-east-1'
    aws_access_key_id= os.environ.get('aws_access_key_id')
    aws_secret_access_key= os.environ.get('aws_secret_access_key')
    s3 = boto3.resource(
        service_name=service_name,
        region_name=region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
        )
    copy_source = {
        'Bucket': 'copyto3bucket111',
        'Key': file_name
    }
    destination_bucket = os.environ['DESTINATION_BUCKET']
    s3.meta.client.copy(copy_source, destination_bucket,file_name)
    
    #send notification
    snsArn = os.environ['SNS_ARN']
    print(snsArn)

    if file_name:
        response = sns_client.publish(TopicArn=	snsArn,
                  Message='file had been copied',
                  Subject='success')

    return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "hello world"
            })
        }