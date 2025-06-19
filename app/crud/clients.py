from sqlalchemy.orm import Session

from app.models.milvus_keys import MilvusKey


def create_client(
    db: Session,
    api_key: str,
    user: str,
    encrypted_uri: str,
    encrypted_token: str,
) -> MilvusKey:
    model = MilvusKey(
        api_key=api_key,
        user=user,
        encrypted_uri=encrypted_uri,
        encrypted_token=encrypted_token,
    )
    db.add(instance=model)
    db.commit()
    db.refresh(instance=model)
    return model
