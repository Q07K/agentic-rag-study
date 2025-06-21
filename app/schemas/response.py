from typing import Any

from pydantic import BaseModel, Field


class ErrorDetail(BaseModel):
    code: str = Field(description="오류 코드")
    message: str = Field(description="오류 메시지")
    details: dict[str, Any] | None = Field(
        description="추가적인 오류 세부 정보",
        default=None,
    )


class ErrorResponse(BaseModel):
    success: bool = Field(
        description="요청 성공 여부",
        default=False,
    )
    error: ErrorDetail = Field(description="오류 세부 정보")


class SuccessResponse[T](BaseModel):
    success: bool = Field(
        description="요청 성공 여부",
        default=True,
    )
    code: str = Field(description="요청 성공 코드")
    message: str | None = Field(
        description="요청에 대한 추가 메시지",
        default=None,
    )
    data: T | None = Field(
        description="요청 결과 데이터",
        default=None,
    )
