from contextlib import contextmanager
from typing import Any, Generator

from pymilvus import MilvusClient


@contextmanager
def zilliz_client_context(
    uri: str,
    token: str,
) -> Generator[MilvusClient, Any, None]:
    """Milvus 클라이언트를 context manager 형태로 제공합니다.

    Parameters
    ----------
    uri : str
        Zilliz Cloud URI
    token : str
        Zilliz Cloud API 토큰

    Yields
    ------
    Generator[MilvusClient, Any, None]
        Milvus 클라이언트 인스턴스
    """
    client = MilvusClient(uri=uri, token=token)
    try:
        yield client
    finally:
        client.close()
