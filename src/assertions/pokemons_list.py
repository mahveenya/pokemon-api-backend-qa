from assertions.common import verify_pokemon_name
from constants import Endpoints
from db.models.pokemon import PokemonModel
from hamcrest import assert_that, equal_to


def _verify_count(res, expected_count):
    assert_that(res["count"], equal_to(expected_count))


def _verify_results_count(res, expected_results_quantity):
    assert_that(len(res["results"]), equal_to(expected_results_quantity))


def _verify_pagination_links(res, expected_next_link=None, expected_previous_link=None):
    assert_that(res["next"], equal_to(expected_next_link))
    assert_that(res["previous"], equal_to(expected_previous_link))


def _verify_pokemon_url(pokemon, pokemon_id):
    actual_pokemon_url = pokemon["url"]
    expected_url = Endpoints.POKEMON_BY_ID_OR_NAME.format(id_or_name=pokemon_id)
    assert_that(actual_pokemon_url, equal_to(expected_url))


def _verify_pokemon_named_resource(pokemon, expected_pokemon: PokemonModel):
    verify_pokemon_name(pokemon, expected_pokemon.name)
    _verify_pokemon_url(pokemon, expected_pokemon.id)


def _verify_pokemon_named_resources_in_results(
    response, expected_pokemons: list[PokemonModel]
):
    results = response["results"]
    for pokemon in expected_pokemons:
        actual_pokemon = results[pokemon.id - 1]
        _verify_pokemon_named_resource(actual_pokemon, pokemon)


def verify_pokemons_list_response(
    response,
    expected_pokemons: list[PokemonModel],
    expected_count,
    expected_pagination_links: dict,
):
    _verify_count(response, expected_count)
    _verify_results_count(response, len(expected_pokemons))
    _verify_pagination_links(
        response,
        expected_next_link=expected_pagination_links["next"],
        expected_previous_link=expected_pagination_links["previous"],
    )
    _verify_pokemon_named_resources_in_results(response, expected_pokemons)
