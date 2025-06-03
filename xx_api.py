from flask_openapi3 import Tag, APIBlueprint
# Pydanticモデル定義をmodels/xx.pyからインポート
from models.xx import XXRequest, XXResponse

bp = APIBlueprint(
    "/xx",
    __name__,
    url_prefix="/api/xx"
)
xx_tag = Tag(name="API分割", description="xxAPIの説明")

@bp.post(
    "/double",
    tags=[xx_tag],
    summary="Double the input value",
    responses={
        200: XXResponse
    }
)
def double_value(query: XXRequest):
    """Double the input value
    """
    return XXResponse(result=query.value * 2).model_dump()
