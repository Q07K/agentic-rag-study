from fastapi import APIRouter

app = APIRouter(
    prefix="/v1/vector",
    tags=["vector"],
)


@app.get("/")
def test():
    return None
