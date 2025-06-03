from flask_openapi3 import Tag, APIBlueprint
from pydantic import BaseModel, Field

bp = APIBlueprint(
    "/xx",
    __name__,
    url_prefix="/api/xx"
)
xx_tag = Tag(name="API分割", description="xxAPIの説明")

# Pydanticモデル定義
class XXRequest(BaseModel):
    value: int = Field(..., ge=0, example=123)
    """Input value to be doubled
    """

class XXResponse(BaseModel):
    result: int = Field(..., example=246)

@bp.post(
    "/double",
    tags=[xx_tag],
    summary="Double the input value",
    responses={
        200: XXResponse
    }
)
def double_value(query: XXRequest):
    """
    Double the input value
    """
    return XXResponse(result=query.value * 2).model_dump()
