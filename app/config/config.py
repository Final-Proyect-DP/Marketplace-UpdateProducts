import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # Fix typo
    SQLALCHEMY_TRACK_MODIFICATIONS = False

print(f"DATABASE_URI: {Config.SQLALCHEMY_DATABASE_URI}")