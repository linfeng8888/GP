import os
import boto3
from botocore.exceptions import ClientError

R2_ACCESS_KEY_ID = os.environ['R2_ACCESS_KEY_ID']
R2_SECRET_ACCESS_KEY = os.environ['R2_SECRET_ACCESS_KEY']
R2_BUCKET_NAME = os.environ['R2_BUCKET_NAME']
R2_ACCOUNT_ID = os.environ['R2_ACCOUNT_ID']

client = boto3.client(
    's3',
    region_name='auto',
    endpoint_url=f'https://{R2_ACCOUNT_ID}.r2.cloudflarestorage.com',
    aws_access_key_id=R2_ACCESS_KEY_ID,
    aws_secret_access_key=R2_SECRET_ACCESS_KEY
)

try:
    response = client.list_objects_v2(Bucket=R2_BUCKET_NAME)
    if 'Contents' in response:
        print("Objects in bucket:")
        for obj in response['Contents']:
            print(obj['Key'])
    else:
        print("Bucket is empty.")
except ClientError as e:
    print("Error accessing bucket:", e)
