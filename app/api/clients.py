from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app.db.sqlite_session import get_db

router = APIRouter(
    prefix="/v1/clients",
    tags=["clients"],
)


@router.post(path="/")
def create_client(db: Session = Depends(dependency=get_db)):
    crud.clients.create_client(
        db=db,
        client_id="example_api_key1",
        user="example_user",
        encrypted_uri="example_encrypted_uri",
        encrypted_token="example_encrypted_token",
    )
    return {"message": "Client created successfully"}


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
