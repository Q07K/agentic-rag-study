from fastapi import APIRouter

router = APIRouter(
    prefix="/v1/clients",
    tags=["clients"],
)


@router.get("/")
def create_client():
    pass


@router.get("/{client_id}")
def get_client():
    pass


@router.put("/{client_id}")
def update_client():
    pass


@router.delete("/{client_id}")
def delete_client():
    pass
