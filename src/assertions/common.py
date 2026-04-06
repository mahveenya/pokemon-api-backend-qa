from hamcrest import assert_that, equal_to


def verify_pokemon_name(pokemon, expected_name):
    assert_that(pokemon["name"], equal_to(expected_name))
