from pydantic import BaseModel, Field

class SampleQueryParams(BaseModel):
    """サンプルのクエリパラメータ"""
    param1: str = Field(..., json_schema_extra={"example": "value1"})
    """パラメータ1
    """
    param2: int = Field(..., ge=0, le=100, json_schema_extra={"example": 50})
    """パラメータ2
    """
    optional_param: str | None = Field(None, json_schema_extra={"example": "optional_value"})
    """オプションのパラメータ
    """

class UserProfile(BaseModel):
    """ユーザープロフィール"""
    name: str = Field(..., min_length=2, max_length=40, json_schema_extra={"example": "very_important_user"})
    """お名前
    """
    age: int = Field(..., ge=1, le=149, json_schema_extra={"example": 42})
    """年齢
    """
    optional_field: str | None = Field(None, json_schema_extra={"example": "optional_value"})
    """オプションのフィールド
    """

class SuccessResponse(BaseModel):
    name: str = Field(..., json_schema_extra={"example": "very_important_user"})
    age: int = Field(..., json_schema_extra={"example": 42})
    optional_field: str | None = Field(None, json_schema_extra={"example": "optional_value"})

class UserNotFoundResponse(BaseModel):
    error: str = Field(..., json_schema_extra={"example": "User not found"})
