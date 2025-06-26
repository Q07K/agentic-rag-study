from fastapi import APIRouter

router = APIRouter(
    prefix="/v1/vectors",
    tags=["vectors"],
)


@router.get("/")
def test():
    return None
