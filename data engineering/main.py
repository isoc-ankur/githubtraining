import os
from dotenv import load_dotenv
import boto3
from botocore.exceptions import ClientError


load_dotenv()

username = os.getenv('username')
password = os.getenv('password')
print(username)