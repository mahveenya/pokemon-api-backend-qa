from assertions.pokemon import verify_pokemon_response
from tests.base_test import BaseTest


class TestPokemons(BaseTest):
    def test_pokemon_is_returned_by_id(self):
        response = self.client.pokemon.get(1)
        expected_pokemon = self.db.pokemon.get_one(id=1)
        expected_pokemon_abilities = self.db.pokemon.get_all_pokemon_abilities(
            pokemon_id=1
        )
        verify_pokemon_response(response, expected_pokemon, expected_pokemon_abilities)
