from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from db.settings import settings


DB_URL = settings.get_db_url()

engine = create_engine(DB_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Session = scoped_session(SessionLocal)
