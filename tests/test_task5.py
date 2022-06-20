"""Task 5"""
import pytest


@pytest.mark.parametrize("city, city_confirmation", [
    ("London", "London"),
    ("Jakarta", "Jakarta"),
])
def test_task5(load_env, city, city_confirmation):
    """See task 5 in the readme"""
    # pylint: disable=unused-argument, unused-import, duplicate-code, comparison-with-itself, singleton-comparison

    assert True
