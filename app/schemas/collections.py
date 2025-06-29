from typing import Any

from pydantic import BaseModel, Field


class ErrorDetail(BaseModel):
    code: str = Field(description="오류 코드")
    message: str = Field(description="오류 메시지")
    details: dict[str, Any] | None = Field(
        description="추가적인 오류 세부 정보",
        default=None,
    )
