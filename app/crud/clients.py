from sqlalchemy.orm import Session

from app.models.client_keys import ClientKey


def create_client(
    db: Session,
    client_id: str,
    user: str,
    encrypted_uri: str,
    encrypted_token: str,
) -> ClientKey:
    model = ClientKey(
        client_id=client_id,
        user=user,
        encrypted_uri=encrypted_uri,
        encrypted_token=encrypted_token,
    )
    db.add(instance=model)
    db.commit()
    db.refresh(instance=model)
    return model


def read_client_by_client_id(db: Session, client_id: str) -> ClientKey | None:
    return db.query(ClientKey).filter(ClientKey.client_id == client_id).first()


def update_client_by_client_id(
    db: Session,
    client_id: str,
    user: str,
    encrypted_uri: str,
    encrypted_token: str,
) -> ClientKey | None:
    model = read_client_by_client_id(db=db, client_id=client_id)
    if model:
        model.user = user
        model.encrypted_uri = encrypted_uri
        model.encrypted_token = encrypted_token
        db.commit()
        db.refresh(instance=model)
    return model


def delete_client_by_client_id(
    db: Session, client_id: str
) -> ClientKey | None:
    model = read_client_by_client_id(db=db, client_id=client_id)
    if model:
        db.delete(instance=model)
        db.commit()
    return model
