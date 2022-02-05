import boto3

client = boto3.client('s3')
paginator = client.get_paginator('list_objects')
s3_bucket = 'mark3bucket'

cnt=1
for each in paginator.paginate(Bucket = s3_bucket):
    for each2 in each['Contents']:
        print(each2['Size'], "bytes ")
        cnt=cnt+1