from pydantic import BaseModel, Field

class XXRequest(BaseModel):
    value: int = Field(..., ge=0, example=123)
    """Input value to be doubled"""

class XXResponse(BaseModel):
    result: int = Field(..., example=246)
