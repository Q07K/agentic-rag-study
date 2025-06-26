from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app.config import config
from app.db.sqlite_session import get_db
from app.schemas.clients import CreateClientRequest, CreateClientResponse
from app.schemas.response import SuccessResponse
from app.services.security import encrypt_value, generate_api_key

router = APIRouter(
    prefix="/v1/clients",
    tags=["clients"],
)


@router.post(path="/", response_model=SuccessResponse[CreateClientResponse])
def create_client(
    request: CreateClientRequest,
    db: Session = Depends(dependency=get_db),
) -> SuccessResponse[CreateClientResponse]:
    clinet_id = generate_api_key()

    encrypted_uri = encrypt_value(
        value=request.uri,
        key=config.encryption_key,
    )
    encrypted_token = encrypt_value(
        value=request.token,
        key=config.encryption_key,
    )

    crud.clients.create_client(
        db=db,
        client_id=clinet_id,
        user=request.user,
        encrypted_uri=encrypted_uri,
        encrypted_token=encrypted_token,
    )
    return SuccessResponse[CreateClientResponse](
        code="client.created",
        message="Client created successfully",
        data=CreateClientResponse(
            client_id=clinet_id,
        ),
    )


@router.get(path="/{client_id}")
def get_client(
    client_id: str,
    db: Session = Depends(dependency=get_db),
):
    return crud.clients.get_client_by_client_id(db=db, client_id=client_id)


@router.put(path="/{client_id}")
def update_client():
    pass


@router.delete(path="/{client_id}")
def delete_client(
    client_id: str,
    db: Session = Depends(dependency=get_db),
):
    return crud.clients.delete_client_by_client_id(
        db=db,
        client_id=client_id,
    )
