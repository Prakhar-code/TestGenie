from pydantic import BaseModel


class OptimizeContract(BaseModel):
    contract: str
