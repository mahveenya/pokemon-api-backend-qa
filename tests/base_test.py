from api.pokemons_list import PokemonsListEndpoint
import pytest


class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, client, db):
        self.db = db
        self.client = client
        self.pokemons_list = PokemonsListEndpoint(client)
