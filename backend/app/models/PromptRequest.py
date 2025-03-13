from pydantic import BaseModel


class PromptRequest(BaseModel):
    contract: str
    language: str
