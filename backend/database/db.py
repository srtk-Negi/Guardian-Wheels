from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')


def get_engine():
    engine = create_engine(
        f'mysql+pymysql://{username}:{password}@{host}/{db_name}')
    return engine
