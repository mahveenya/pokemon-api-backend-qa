from db.models.ability import AbilityModel
from db.models.pokemon import PokemonModel


class PokemonTable:
    def __init__(self, client):
        self.client = client

    def count_all_entries(self):
        return self.client.count_all_entries("pokemon")

    def get_one(self, **kwargs):
        row = self.client.select("pokemon", fetch="one", **kwargs)
        return PokemonModel(**row)

    def get_all(self, **kwargs):
        rows = self.client.select("pokemon", fetch="all", **kwargs)
        return [PokemonModel(**row) for row in rows]

    def get_all_pokemon_abilities(self, pokemon_id):
        rows = self.client.select(
            "pokemon_ability",
            fetch="all",
            pokemon_id=pokemon_id,
        )
        ability_ids = [row["ability_id"] for row in rows]
        return [
            AbilityModel(**self.client.select("ability", fetch="one", id=ability_id))
            for ability_id in ability_ids
        ]
