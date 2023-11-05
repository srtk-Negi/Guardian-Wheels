from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')


def get_connection():
    engine = create_engine(
        f'mysql+pymysql://{username}:{password}@{host}/{db_name}')
    return engine


def main():
    with get_connection().begin() as conn:
        result = conn.execute(text('SELECT * FROM test'))
    for row in result:
        print(row)


if __name__ == '__main__':
    main()
