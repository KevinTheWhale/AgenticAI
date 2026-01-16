# FOR STRUCTURED OUTPUT TO PREVENT HALLUCINATION
from pydantic import BaseModel
from typing import Optional

class AgentDecision(BaseModel):
    action: str               # "run_query" | "inspect_schema" | "refuse", i.e. the only set of tools the agent has
    sql: Optional[str] = None
    reason: Optional[str] = None