from flask_openapi3 import OpenAPI, Info, Tag
from models.user import UserProfile, SuccessResponse, UserNotFoundResponse

info = Info(title='Sample API', version='1.0', description='A simple User API')
app = OpenAPI(__name__, info=info)
user_tag = Tag(name="user", description="User operations")

@app.get(
    "/api/user",
    tags=[user_tag],
    summary="get user profile (summary of this endpoint)",
    responses={
        200: SuccessResponse
    },
)
def get_user_profile():
    """
    Get user profile by query parameters (name, age)
    """
    try:
        # クエリパラメータをPydanticモデルでバリデーション
        user = UserProfile(name="お名前", age=22)
        return SuccessResponse(name=user.name, age=user.age).model_dump()
    except Exception as e:
        return {"error": str(e)}, 400

@app.post(
    "/api/user",
    tags=[user_tag],
    summary="verify user profile (summary of this endpoint)",
    responses={
        200: SuccessResponse,
        404: UserNotFoundResponse
    },
)
def user_profile(body: UserProfile):
    """ここにこのAPIの説明を書きます
    """
    # 何らかの条件で404を返すサンプル（例: nameが"notfound"なら404）
    if body.name == "notfound":
        return UserNotFoundResponse(error="User not found").model_dump(), 404
    # バリデーションは自動、受け取ったデータをそのまま返す
    try:
        return SuccessResponse(name=body.name, age=body.age).model_dump()
    except Exception as e:
        return {"error": str(e)}, 400

# xx_apiのBlueprintを登録
from xx_api import bp as xx_bp
app.register_api(xx_bp)

if __name__ == "__main__":
    app.run(port=8000, debug=True, use_reloader=True)
