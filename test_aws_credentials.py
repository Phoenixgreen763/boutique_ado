import os
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def test_aws_credentials():
    # Print environment variables for debugging
    print("AWS_ACCESS_KEY_ID:", os.environ.get('AWS_ACCESS_KEY_ID'))
    print("AWS_SECRET_ACCESS_KEY:", os.environ.get('AWS_SECRET_ACCESS_KEY'))
    
    try:
        # Create an S3 client using environment variables for credentials
        s3 = boto3.client(
            's3',
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
            region_name='eu-north-1'
        )
        
        # Try listing buckets to confirm credentials are working
        response = s3.list_buckets()
        print("AWS Credentials are correct. Buckets:")
        for bucket in response['Buckets']:
            print(f"  - {bucket['Name']}")
            
    except NoCredentialsError:
        print("No AWS credentials found.")
    except PartialCredentialsError:
        print("Partial AWS credentials found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the test function
test_aws_credentials()
