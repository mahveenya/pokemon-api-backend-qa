from db.models.effect_entry import EffectEntryModel
from pydantic import BaseModel


class AbilityModel(BaseModel):
    id: int
    name: str
    effect_entries: list[EffectEntryModel]
