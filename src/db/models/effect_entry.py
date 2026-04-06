from db.models.language import LanguageModel
from pydantic import BaseModel


class EffectEntryModel(BaseModel):
    effect: str
    short_effect: str
    language: LanguageModel
