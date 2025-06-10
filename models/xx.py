from pydantic import BaseModel, Field

class XXRequest(BaseModel):
    value: int = Field(..., ge=0, json_schema_extra={"example": 123})
    """Input value to be doubled"""

class XXResponse(BaseModel):
    result: int = Field(..., json_schema_extra={"example": 246})
