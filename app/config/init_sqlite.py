from app.db.sqlite_base import Base
from app.db.sqlite_session import engine
from app.models.milvus_keys import MilvusKey

_ = MilvusKey


def init_db() -> None:
    """데이터베이스를 초기화합니다.

    전역 SQLAlchemy `engine`에 연결된 데이터베이스에 필요한 `MilvusKey` 테이블을
    생성하여 데이터베이스 스키마를 설정합니다.

    Returns:
        None
    """
    Base.metadata.create_all(bind=engine)
