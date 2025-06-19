from fastapi import APIRouter

router = APIRouter(
    prefix="/v1/milvus/client",
    tags=["collections"],
)


@router.get("/")
def test(): ...
