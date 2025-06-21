from pydantic import BaseModel


class CreateClientRequest(BaseModel):
    user: str
    uri: str
    token: str


class CreateClientResponse(BaseModel):
    client_id: str


class ReadClientResponse(BaseModel):
    user: str
    client_id: str


class UpdateClientRequest(BaseModel):
    user: str | None = None
    uri: str | None = None
    token: str | None = None


class UpdateClientResponse(BaseModel):
    message: str
    client_id: str


class DeleteClientResponse(BaseModel):
    message: str
    client_id: str
