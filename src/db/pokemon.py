from db.models.pokemon import PokemonModel


class PokemonTable:
    def __init__(self, client):
        self.client = client

    def count_all_entries(self):
        return self.client.count_all_entries("pokemon")

    def get_one(self, **kwargs):
        rows = self.client.select("pokemon", fetch="one", **kwargs)
        return PokemonModel(**rows)

    def get_all(self, **kwargs):
        rows = self.client.select("pokemon", fetch="all", **kwargs)
        return [PokemonModel(**row) for row in rows]
