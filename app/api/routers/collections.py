from typing import Any

from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies.zilliz_dependency import (
    get_authenticated_zilliz_client,
)
from app.crud.vectors import create_milvus_collection
from app.schemas.response import SuccessResponse

router = APIRouter(
    prefix="/v1/collections",
    tags=["collections"],
)


@router.post(path="/", response_model=SuccessResponse[Any])
async def create_collection(
    zilliz_context=Depends(dependency=get_authenticated_zilliz_client),
) -> SuccessResponse[Any]:
    with zilliz_context as zilliz_client:
        created_flag = create_milvus_collection(client=zilliz_client)

    if not created_flag:
        raise HTTPException(
            status_code=409,
            detail="Collection already exists.",
        )

    return SuccessResponse(
        code="collection.created",
        message="Collection created successfully",
        data=None,
    )


@router.get(path="/", response_model=SuccessResponse[Any])
async def read_collections(
    zilliz_context=Depends(dependency=get_authenticated_zilliz_client),
) -> SuccessResponse[Any]:
    with zilliz_context as zilliz_client:
        return SuccessResponse(
            code="collections.read",
            message="Collections read successfully",
            data=zilliz_client.list_collections(),
        )


@router.delete(path="/{collection_name}", response_model=SuccessResponse[Any])
async def delete_collection(
    collection_name: str,
    zilliz_context=Depends(dependency=get_authenticated_zilliz_client),
) -> SuccessResponse[Any]:
    with zilliz_context as zilliz_client:
        zilliz_client.drop_collection(collection_name=collection_name)
        return SuccessResponse(
            code="collection.deleted",
            message=f"Collection '{collection_name}' deleted successfully",
            data=None,
        )
