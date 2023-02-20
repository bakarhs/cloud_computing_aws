import boto3
# Creating s3 bucket using python-boto3
s3_client = boto3.client('s3')

response = s3_client.create_bucket(
    ACL='private'|'public-read',
    Bucket='abubakar-tech201',
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-1'
    },
)

# Upload file to s3 using boto3
bucket = response.Bucket("abubakar-tech201-python")
bucket.upload_file('C:/Users/ashar/Documents/SG/test1.txt', 'test.txt')

# Retrieve file from S3 using python-boto3
bucket.download_file('test.txt', 'C:/Users/ashar/Documents/SG/test1.txt')

# Delete Content from S3 using python-boto3
bucket.Object('test.txt').delete()

# Delete the bucket using python-boto3
response.Bucket('abubakar-tech201-python').delete()




