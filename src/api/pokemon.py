from api.core_client import CoreClient
from constants import Endpoints


class PokemonEndpoint:
    def __init__(self, core_client: CoreClient):
        self.core_client = core_client
        self.path = Endpoints.POKEMON_BY_ID_OR_NAME

    def get(self, id_or_name: int | str, **kwargs):
        return self.core_client.get(self.path.format(id_or_name=id_or_name), **kwargs)
