from pydantic import BaseModel


class PokemonModel(BaseModel):
    id: int
    name: str
