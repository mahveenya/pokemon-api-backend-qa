from assertions.pokemons_list import verify_count, verify_results_count
from constants import DefaultValues
from tests.base_test import BaseTest


class TestPokemonsList(BaseTest):
    def test_default_pokemon_quantity_is_returned(self):
        res = self.pokemons_list.get()
        expected_count = self.db.pokemon.count_all_entries()
        verify_count(res, expected_count)
        verify_results_count(res, DefaultValues.DEFAULT_LIMIT)
