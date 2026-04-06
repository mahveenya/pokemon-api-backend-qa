from pydantic import BaseModel


class LanguageModel(BaseModel):
    name: str
