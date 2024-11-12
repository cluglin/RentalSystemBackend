from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.datebase import DatabaseEnv
from typing import cast

engine = create_engine(cast(str, DatabaseEnv.CONNECT_STRING), echo=False, pool_size=5, max_overflow=5)
SessionLocal = sessionmaker(autocommit=False, bind=engine)


def create_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
