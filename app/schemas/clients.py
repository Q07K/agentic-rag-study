from pydantic import BaseModel


class ClientRequest(BaseModel):
    user: str
    uri: str
    token: str


class ClientResponse(BaseModel):
    client_id: str


class ReadClientResponse(BaseModel):
    user: str
    client_id: str
