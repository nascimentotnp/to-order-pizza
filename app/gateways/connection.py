import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


load_dotenv()

db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

connection_db_url = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'


engine = create_engine(connection_db_url, echo=False)

Session = sessionmaker(bind=engine)
session = Session()
