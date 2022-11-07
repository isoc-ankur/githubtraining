import os
from dotenv import load_dotenv
import pandas

load_dotenv()

username = os.getenv('username')
password = os.getenv('password')
print(username)