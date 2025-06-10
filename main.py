from flask import redirect
from flask_openapi3 import OpenAPI, Info, Tag
from models.user import SampleQueryParams, UserProfile, SuccessResponse, UserNotFoundResponse
import toml

# pyproject.tomlからプロジェクト情報を取得
with open("pyproject.toml", encoding="utf-8") as f:
    pyproject = toml.load(f)
project = pyproject.get("project", {})
title = project.get("name", "Sample API")
version = project.get("version", "1.0")
description = project.get("description", "A simple User API")

info = Info(title=title, version=version, description=description)
app = OpenAPI(__name__, info=info)
user_tag = Tag(name="user", description="User operations")

# / にアクセスが来たときSwagger UIにリダイレクト
@app.get("/")
def root():
    """Redirect to Swagger UI"""
    return redirect("/openapi/swagger")

@app.get(
    "/api/user",
    tags=[user_tag],
    summary="get user profile (summary of this endpoint)",
    responses={
        200: SuccessResponse
    },
)
def get_user_profile():
    """Get user profile by query parameters (name, age)"""
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
def user_profile(query: SampleQueryParams, body: UserProfile):
    """ユーザープロファイルを検証します。
    
    クエリのサンプル:
    ?name=sampleuser&age=22
    
    リクエストボディの例:
    {
        "name": "sampleuser",
        "age": 22
    }
    """
    # クエリのname, ageがNoneでなければ優先、なければbodyの値
    user_name = query.param1 if query.param1 is not None else body.name
    user_age = query.param2 if query.param2 is not None else body.age
    # 404サンプル
    if user_name == "notfound":
        return UserNotFoundResponse(error="User not found").model_dump(), 404
    try:
        return SuccessResponse(name=user_name, age=user_age).model_dump()
    except Exception as e:
        return {"error": str(e)}, 400

# xx_apiのBlueprintを登録
from xx_api import bp as xx_bp
app.register_api(xx_bp)

if __name__ == "__main__":
    app.run(port=8000, debug=True, use_reloader=True)
