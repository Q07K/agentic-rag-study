from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import config

SQLITE_DB_URL = f"sqlite:///{config.sqlite_db_path}"

engine = create_engine(
    url=SQLITE_DB_URL,
    connect_args={"check_same_thread": False},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
