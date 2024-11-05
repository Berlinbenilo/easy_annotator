import os

from dotenv import load_dotenv


def get_mongo_credentials():
    load_dotenv()

    MONGO_USER = os.environ['MONGO_USER_NAME'] if os.environ.get('MONGO_USER_NAME') else 'root'
    MONGO_PASSWORD = os.environ['MONGO_PASSWORD'] if os.environ.get('MONGO_PASSWORD') else 'root'
    MONGO_HOST = os.environ['MONGO_HOST'] if os.environ.get('MONGO_HOST') else 'localhost'
    MONGO_PORT = os.environ['MONGO_PORT'] if os.environ.get('MONGO_PORT') else 27017
    MONGO_DB_NAME = os.environ['MONGO_DB_NAME'] if os.environ.get('MONGO_DB_NAME') else 'annotator'
    return MONGO_USER, MONGO_PASSWORD, MONGO_HOST, MONGO_PORT, MONGO_DB_NAME
