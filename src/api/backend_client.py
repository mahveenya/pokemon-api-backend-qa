from api.core_client import CoreClient
from api.pokemon import PokemonEndpoint
from api.pokemon_list import PokemonListEndpoint


class BackendClient:
    def __init__(self, core_client: CoreClient):
        self.pokemon_list = PokemonListEndpoint(core_client)
        self.pokemon = PokemonEndpoint(core_client)
