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
    responses={
        422: {"description": "요청 데이터 형식이 올바르지 않습니다"},
    },
)


@router.post(path="/", response_model=SuccessResponse[ClientResponse])
async def create_client(
    body: ClientRequest,
    db: Session = Depends(dependency=get_db),
) -> SuccessResponse[ClientResponse]:
    """
    클라이언트 생성

    새로운 클라이언트를 생성합니다.
    - **user**: 사용자 이름
    - **uri**: Milvus URI
    - **token**: Milvus 토큰

    Returns:
        SuccessResponse[ClientResponse]: 생성된 클라이언트 정보
    """
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


@router.get(
    path="/",
    response_model=SuccessResponse[ClientResponse],
    responses={
        401: {"description": "인증 토큰이 유효하지 않습니다"},
        404: {"description": "클라이언트를 찾을 수 없습니다"},
    },
)
async def read_client_by_token(
    client_id: str = Depends(dependency=get_client_id_from_token),
    db: Session = Depends(dependency=get_db),
) -> SuccessResponse[ClientResponse]:
    """
    클라이언트 조회

    클라이언트 ID를 통해 클라이언트 정보를 조회합니다.
    인증 토큰에서 클라이언트 ID를 추출하여 사용합니다.

    Returns:
        SuccessResponse[ClientResponse]: 클라이언트 정보

    Raises:
        HTTPException: 클라이언트를 찾을 수 없는 경우 (404)
    """
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


@router.put(
    path="/",
    response_model=SuccessResponse[ClientResponse],
    responses={
        401: {"description": "인증 토큰이 유효하지 않습니다"},
        404: {"description": "클라이언트를 찾을 수 없습니다"},
    },
)
async def update_client(
    body: ClientRequest,
    client_id: str = Depends(dependency=get_client_id_from_token),
    db: Session = Depends(dependency=get_db),
) -> SuccessResponse[ClientResponse]:
    """
    클라이언트 정보 수정

    기존 클라이언트의 정보를 수정합니다.
    - **user**: 새로운 사용자 이름
    - **uri**: 새로운 Milvus URI
    - **token**: 새로운 Milvus 토큰

    Returns:
        SuccessResponse[ClientResponse]: 수정된 클라이언트 정보

    Raises:
        HTTPException: 클라이언트를 찾을 수 없는 경우 (404)
    """
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


@router.delete(
    path="/",
    responses={
        401: {"description": "인증 토큰이 유효하지 않습니다"},
        404: {"description": "클라이언트를 찾을 수 없습니다"},
    },
)
async def delete_client(
    client_id: str = Depends(dependency=get_client_id_from_token),
    db: Session = Depends(dependency=get_db),
):
    """
    클라이언트 삭제

    기존 클라이언트를 삭제합니다.
    인증 토큰에서 클라이언트 ID를 추출하여 해당 클라이언트를 삭제합니다.

    Returns:
        SuccessResponse[ClientResponse]: 삭제된 클라이언트 정보

    Raises:
        HTTPException: 클라이언트를 찾을 수 없는 경우 (404)
    """
    model = crud.clients.read_client_by_client_id(db=db, client_id=client_id)

    if not model:
        raise HTTPException(
            status_code=404,
            detail="Client not found",
        )

    crud.clients.delete_client_by_client_id(db=db, client_id=client_id)

    return SuccessResponse[ClientResponse](
        code="client.deleted",
        message="Client deleted successfully",
        data=ClientResponse(
            client_id=client_id,
        ),
    )
