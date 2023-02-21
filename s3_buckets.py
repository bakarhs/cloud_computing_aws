import boto3
# Creating s3 bucket using python-boto3
s3_client = boto3.client('s3')

s3 = boto3.resource('s3')
s3.create_bucket(Bucket='abubakar-tech201-python', CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})

# Upload file to s3 using boto3
bucket = s3.Bucket("abubakar-tech201-python")
bucket.upload_file('/home/ubuntu/test.txt', 'test.txt')

# Retrieve file from S3 using python-boto3
bucket.download_file('test.txt', '/home/ubuntu/test.txt')

# Delete Content from S3 using python-boto3
bucket.Object('test.txt').delete()

# Delete the bucket using python-boto3
s3.Bucket('abubakar-tech201-python').delete()




