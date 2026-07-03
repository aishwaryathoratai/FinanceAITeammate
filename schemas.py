from typing import List
from pydantic import BaseModel, Field

class AgentRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=3,
        max_length=500,
        description="User question"
    )
class AgentResponse(BaseModel):
    answer: str
    sources: List[str]