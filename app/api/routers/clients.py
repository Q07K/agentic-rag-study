from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api.dependencies.auth import get_client_id_from_token
from app.config import configs
from app.db.sqlite_session import get_db
from app.schemas.clients import ClientRequest, ClientResponse
from app.schemas.response import SuccessResponse
from app.services.security import encrypt_value, generate_api_key

router = APIRouter(
    prefix="/v1/clients",
    tags=["clients"],
)


@router.post(path="/", response_model=SuccessResponse[ClientResponse])
def create_client(
    body: ClientRequest,
    db: Session = Depends(dependency=get_db),
) -> SuccessResponse[ClientResponse]:
    client_id = generate_api_key()

    encrypted_uri = encrypt_value(
        value=body.uri,
        key=configs.encryption_key,
    )
    encrypted_token = encrypt_value(
        value=body.token,
        key=configs.encryption_key,
    )

    crud.clients.create_client(
        db=db,
        client_id=client_id,
        user=body.user,
        encrypted_uri=encrypted_uri,
        encrypted_token=encrypted_token,
    )
    return SuccessResponse[ClientResponse](
        code="client.created",
        message="Client created successfully",
        data=ClientResponse(
            client_id=client_id,
        ),
    )


@router.get(path="/", response_model=SuccessResponse[ClientResponse])
def get_client(
    client_id: str = Depends(dependency=get_client_id_from_token),
    db: Session = Depends(dependency=get_db),
):
    model = crud.clients.read_client_by_client_id(db=db, client_id=client_id)

    if not model:
        raise HTTPException(
            status_code=404,
            detail="Client not found",
        )
    return SuccessResponse[ClientResponse](
        code="client.read",
        message="Client read successfully",
        data=ClientResponse(
            client_id=client_id,
        ),
    )


@router.put(path="/", response_model=SuccessResponse[ClientResponse])
def update_client(
    body: ClientRequest,
    client_id: str = Depends(dependency=get_client_id_from_token),
    db: Session = Depends(dependency=get_db),
):
    model = crud.clients.read_client_by_client_id(db=db, client_id=client_id)

    if not model:
        raise HTTPException(
            status_code=404,
            detail="Client not found",
        )

    encrypted_uri = encrypt_value(
        value=body.uri,
        key=configs.encryption_key,
    )
    encrypted_token = encrypt_value(
        value=body.token,
        key=configs.encryption_key,
    )
    crud.clients.update_client_by_client_id(
        db=db,
        client_id=client_id,
        user=body.user,
        encrypted_uri=encrypted_uri,
        encrypted_token=encrypted_token,
    )
    return SuccessResponse[ClientResponse](
        code="client.updated",
        message="Client updated successfully",
        data=ClientResponse(
            client_id=client_id,
        ),
    )


@router.delete(path="/")
def delete_client(
    client_id: str = Depends(dependency=get_client_id_from_token),
    db: Session = Depends(dependency=get_db),
):
    return crud.clients.delete_client_by_client_id(
        db=db,
        client_id=client_id,
    )
