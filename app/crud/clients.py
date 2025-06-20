from sqlalchemy.orm import Session

from app.models.milvus_keys import MilvusKey


def create_client(
    db: Session,
    client_id: str,
    user: str,
    encrypted_uri: str,
    encrypted_token: str,
) -> MilvusKey:
    model = MilvusKey(
        client_id=client_id,
        user=user,
        encrypted_uri=encrypted_uri,
        encrypted_token=encrypted_token,
    )
    db.add(instance=model)
    db.commit()
    db.refresh(instance=model)
    return model


def get_client_by_client_id(db: Session, client_id: str) -> MilvusKey | None:
    return db.query(MilvusKey).filter(MilvusKey.client_id == client_id).first()


def delete_client_by_client_id(
    db: Session, client_id: str
) -> MilvusKey | None:
    model = (
        db.query(MilvusKey).filter(MilvusKey.client_id == client_id).first()
    )
    if model:
        db.delete(instance=model)
        db.commit()
    return model
