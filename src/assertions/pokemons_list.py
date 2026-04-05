from hamcrest import assert_that, equal_to


def verify_count(res, expected_count):
    assert_that(res["count"], equal_to(expected_count))


def verify_results_count(res, expected_results_quantity):
    assert_that(len(res["results"]), equal_to(expected_results_quantity))
