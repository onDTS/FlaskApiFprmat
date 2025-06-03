
from flask_openapi3 import OpenAPI, Info, Tag
from pydantic import BaseModel, Field

info = Info(title='Sample API', version='1.0', description='A simple User API')
app = OpenAPI(__name__, info=info)
user_tag = Tag(name="タグ名", description="タグの説明")

# Pydanticモデル定義
class UserProfile(BaseModel):
    """ユーザープロフィール
    """
    name: str = Field(..., min_length=2, max_length=40, example="very_important_user")
    """お名前
    """
    age: int = Field(..., ge=1, le=149, example=42)
    """年齢
    """

# レスポンスモデル: 送信されたUserProfileをそのまま返す
class SuccessResponse(BaseModel):
    name: str = Field(..., example="very_important_user")
    age: int = Field(..., example=42)

class ValidationErrorResponse(BaseModel):
    error: str = Field(..., example="Validation error")

@app.post(
    "/api/user",
    tags=[user_tag],
    summary="verify user profile (summary of this endpoint)",
    responses={
        200: SuccessResponse,
        400: ValidationErrorResponse
    },
)
def user_profile(query: UserProfile):
    """ここにこのAPIの説明を書きます
    """
    # バリデーションは自動、受け取ったデータをそのまま返す
    try:
        # Pydanticモデルをdictに変換して返すことでFlaskが正しくレスポンスを生成できる
        return SuccessResponse(name=query.name, age=query.age).model_dump()
    except Exception as e:
        return {"error": str(e)}, 400


# xx_apiのBlueprintを登録
from xx_api import bp as xx_bp
app.register_api(xx_bp)

if __name__ == "__main__":
    app.run(port=8000, debug=True, use_reloader=True)
