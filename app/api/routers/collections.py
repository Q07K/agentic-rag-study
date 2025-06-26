from fastapi import APIRouter


router = APIRouter(
    prefix="/v1/collections",
    tags=["collections"],
)


@router.get("/")
def test(): ...
