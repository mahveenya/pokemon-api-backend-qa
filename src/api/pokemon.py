from constants import Endpoints


class PokemonEndpoint:
    def __init__(self, client):
        self.client = client
        self.path = Endpoints.POKEMON_BY_ID_OR_NAME

    def get(self, id_or_name: int | str, **kwargs):
        return self.client.get(self.path.format(id_or_name=id_or_name), **kwargs)
