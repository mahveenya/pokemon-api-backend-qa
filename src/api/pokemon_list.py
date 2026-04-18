from api.core_client import CoreClient
from constants import Endpoints


class PokemonListEndpoint:
    def __init__(self, core_client: CoreClient):
        self.core_client = core_client
        self.path = Endpoints.POKEMON

    def get(self, **kwargs):
        return self.core_client.get(self.path, **kwargs)
