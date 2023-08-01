import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

db_url = os.environ.get('DATABASE_URL')
engine = create_engine(db_url, echo=True)
Base = declarative_base()
