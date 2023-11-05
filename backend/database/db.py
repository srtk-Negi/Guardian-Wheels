from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

username = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

conn_string = f"mysql+pymysql://{username}:{password}@{host}/{db_name}"

engine = create_engine(conn_string)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
