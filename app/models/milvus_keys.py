from sqlalchemy import Column, Integer, String

from app.db.sqlite_base import Base


class MilvusKey(Base):
    __tablename__ = "milvus_keys"

    id = Column(Integer, primary_key=True, index=True)
    api_key = Column(String, unique=True, nullable=False)
    user = Column(String, nullable=False)
    encrypted_uri = Column(String, nullable=False)
    encrypted_token = Column(String, nullable=False)
