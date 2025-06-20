from sqlalchemy import Column, Integer, String

from app.db.sqlite_base import Base


class MilvusKey(Base):
    __tablename__ = "milvus_keys"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    client_id = Column(String, unique=True, nullable=False, index=True)
    user = Column(String, nullable=False)
    encrypted_uri = Column(String, nullable=False)
    encrypted_token = Column(String, nullable=False)
