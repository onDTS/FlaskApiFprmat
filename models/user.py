from pydantic import BaseModel, Field

class UserProfile(BaseModel):
    """ユーザープロフィール"""
    name: str = Field(..., min_length=2, max_length=40, example="very_important_user")
    """お名前
    """
    age: int = Field(..., ge=1, le=149, example=42)
    """年齢
    """
    optional_field: str | None = Field(None, example="optional_value")
    """オプションのフィールド
    """

class SuccessResponse(BaseModel):
    name: str = Field(..., example="very_important_user")
    age: int = Field(..., example=42)
    optional_field: str | None = Field(None, example="optional_value")

class UserNotFoundResponse(BaseModel):
    error: str = Field(..., example="User not found")
