from contextlib import _GeneratorContextManager

from fastapi import Depends, HTTPException
from pymilvus.milvus_client.milvus_client import MilvusClient
from sqlalchemy.orm import Session

from app.api.dependencies.auth_dependency import get_client_id_from_token
from app.config import configs
from app.crud.clients import read_client_by_client_id
from app.db.milvus_connect import zilliz_client_context
from app.db.sqlite_session import get_db
from app.services.security import decrypt_value


def get_authenticated_zilliz_client(
    client_id: str = Depends(dependency=get_client_id_from_token),
    db: Session = Depends(dependency=get_db),
) -> _GeneratorContextManager[MilvusClient, None, None]:
    client_model = read_client_by_client_id(db=db, client_id=client_id)
    if not client_model:
        raise HTTPException(status_code=404, detail="Client not found")

    uri = decrypt_value(
        token=client_model.encrypted_uri,
        key=configs.encryption_key,
    )
    token = decrypt_value(
        token=client_model.encrypted_token,
        key=configs.encryption_key,
    )

    return zilliz_client_context(uri=uri, token=token)
