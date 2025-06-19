from fastapi import APIRouter

router = APIRouter(
    prefix="/v1/vector",
    tags=["vector"],
)


@router.get("/")
def test():
    return None
